from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from authentication.models import User
from authentication.serializers import AdminUserSerializer

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from sequences import get_next_value

from drf_spectacular.utils import  extend_schema, OpenApiParameter

from account.models import AccountLog, Group, LedgerAccount, ReceiptVoucher
from authentication.decorators import has_permissions

from donation.models import Donation
from donation.serializers import DonationSerializer, DonationListSerializer
from donation.filters import DonationFilter

from commons.enums import PermissionEnum
from commons.pagination import Pagination

import datetime
from decimal import Decimal



# Create your views here.

@extend_schema(
	parameters=[
		OpenApiParameter("page"),
		OpenApiParameter("size"),
  ],
	request=DonationSerializer,
	responses=DonationSerializer
)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PAYMENT_METHOD_LIST.name])
def getAllDonation(request):
	donations = Donation.objects.all()
	total_elements = donations.count()

	page = request.query_params.get('page')
	size = request.query_params.get('size')

	# Pagination
	pagination = Pagination()
	pagination.page = page
	pagination.size = size
	donations = pagination.paginate_data(donations)

	serializer = DonationSerializer(donations, many=True)

	response = {
		'donations': serializer.data,
		'page': pagination.page,
		'size': pagination.size,
		'total_pages': pagination.total_pages,
		'total_elements': total_elements,
	}

	return Response(response, status=status.HTTP_200_OK)




@extend_schema(request=DonationSerializer, responses=DonationSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PAYMENT_METHOD_DETAILS.name])
def getADonation(request, pk):
	try:
		donation = Donation.objects.get(pk=pk)
		serializer = DonationSerializer(donation)
		return Response(serializer.data, status=status.HTTP_200_OK)
	except ObjectDoesNotExist:
		return Response({'detail': f"Donation id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)




@extend_schema(request=DonationSerializer, responses=DonationSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PERMISSION_DETAILS_VIEW.name])
def searchDonation(request):
	donations = DonationFilter(request.GET, queryset=Donation.objects.all())
	donations = donations.qs

	print('searched_products: ', donations)

	total_elements = donations.count()

	page = request.query_params.get('page')
	size = request.query_params.get('size')

	# Pagination
	pagination = Pagination()
	pagination.page = page
	pagination.size = size
	donations = pagination.paginate_data(donations)

	serializer = DonationListSerializer(donations, many=True)

	response = {
		'donations': serializer.data,
		'page': pagination.page,
		'size': pagination.size,
		'total_pages': pagination.total_pages,
		'total_elements': total_elements,
	}

	if len(donations) > 0:
		return Response(response, status=status.HTTP_200_OK)
	else:
		return Response({'detail': f"There are no donations matching your search"}, status=status.HTTP_400_BAD_REQUEST)




@extend_schema(request=DonationSerializer, responses=DonationSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PAYMENT_METHOD_CREATE.name])
def createDonation(request):
	data = request.data
	print('data: ', data)
	filtered_data = {}

	for key, value in data.items():
		if value != '' and value != 0 and value != '0' and value != 'undefined':
			filtered_data[key] = value

	first_name = filtered_data['first_name']
	last_name = filtered_data['last_name']
	email = filtered_data['email']
	amount = Decimal(filtered_data['amount'])
	payment_method = filtered_data['payment_method']
	phone_number = filtered_data['phone_number']
 
	filtered_data['street_address_one'] = filtered_data.get('address', '')
	filtered_data['password'] = first_name


	serializer = DonationSerializer(data=filtered_data)
	if serializer.is_valid():
		serializer.save()

		user_obj, created = User.objects.get_or_create(email=email, defaults={'first_name':first_name, 'last_name':last_name, 'primary_phone':phone_number})

		group_obj = Group.objects.get(name='Sundry Creditors')
		user_id = user_obj.id
		user_ledger, created = LedgerAccount.objects.get_or_create(reference_id=user_id, defaults={'name':first_name, 'reference_id':user_id, "head_group":group_obj, 'ledger_type':'user_ledger'})
		print('user ledger: ', user_ledger)

		if payment_method != 'offline' or 'Offline':
			current_datetime = str(timezone.now())

			current_date = datetime.date.today()
			current_date = str(current_date)
			current_date = current_date.replace('-', '')
			rv_current_date = 'RV' + current_date
			print('current_date: ', current_date, type(current_date))

			_num = get_next_value(rv_current_date)
			print('get_next_value: ', _num)

			invoice = 'RV' + current_date + '00' + str(_num)
			print('invoice: ', invoice)

			cash_ledger = LedgerAccount.objects.get(name='Cash')
			ReceiptVoucher.objects.create(ledger=cash_ledger, invoice_no=invoice, debit_amount=amount, receipt_date=current_datetime)
			ReceiptVoucher.objects.create(ledger=user_ledger, invoice_no=invoice, credit_amount=amount, receipt_date=current_datetime)

			AccountLog.objects.create(ledger=cash_ledger, reference_no=invoice, debit_amount=amount, log_date=current_datetime, log_type='receipt_voucher')
			AccountLog.objects.create(ledger=user_ledger, reference_no=invoice, credit_amount=amount, log_date=current_datetime, log_type='receipt_voucher')

		return Response(serializer.data, status=status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@extend_schema(request=DonationSerializer, responses=DonationSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PAYMENT_METHOD_UPDATE.name])
def updateDonation(request,pk):
	data = request.data
	print('data: ', data)
	filtered_data = {}

	for key, value in data.items():
		if value != '' and value != 0 and value != '0' and value != 'undefined':
			filtered_data[key] = value

	try:
		donation = Donation.objects.get(pk=pk)

		serializer = DonationSerializer(donation, data=filtered_data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_200_OK)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	except ObjectDoesNotExist:
		return Response({'detail': f"Donation id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)




@extend_schema(request=DonationSerializer, responses=DonationSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PAYMENT_METHOD_DELETE.name])
def deleteDonation(request, pk):
	try:
		donation = Donation.objects.get(pk=pk)
		donation.delete()
		return Response({'detail': f'Donation id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
	except ObjectDoesNotExist:
		return Response({'detail': f"Donation id - {pk} doesn't exists"}, status=status.HTTP_400_BAD_REQUEST)


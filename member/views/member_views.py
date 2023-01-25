from ast import keyword

import requests
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.db.models import Q

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from drf_spectacular.utils import  extend_schema, OpenApiParameter
from sms import send_sms

from account.models import Group, LedgerAccount
from authentication.serializers import AdminUserMinimalListSerializer
from authentication.decorators import has_permissions

from member.models import Member
from member.serializers import MemberSerializer, MemberListSerializer

from utils.login_logout import get_all_logged_in_users

from commons.pagination import Pagination
from commons.enums import PermissionEnum

import datetime




# Create your views here.

@extend_schema(
	parameters=[
		OpenApiParameter("page"),
		OpenApiParameter("size"),
  ],
	request=MemberSerializer,
	responses=MemberListSerializer
)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_LIST.name])
def getAllMember(request):
	members = Member.objects.all()
	total_elements = members.count()

	page = request.query_params.get('page')
	size = request.query_params.get('size')

	# Pagination
	pagination = Pagination()
	pagination.page = page
	pagination.size = size
	members = pagination.paginate_data(members)

	serializer = MemberListSerializer(members, many=True)

	response = {
		'members': serializer.data,
		'page': pagination.page,
		'size': pagination.size,
		'total_pages': pagination.total_pages,
		'total_elements': total_elements,
	}

	return Response(response, status=status.HTTP_200_OK)




@extend_schema(
	parameters=[
		OpenApiParameter("page"),
		OpenApiParameter("size"),
  ],
	request=MemberSerializer,
	responses=MemberListSerializer
)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_LIST.name])
def getAllMemberWithoutPagination(request):
	members = Member.objects.all()

	serializer = MemberListSerializer(members, many=True)

	response = {
		'members': serializer.data,
	}

	return Response(response, status=status.HTTP_200_OK)




@extend_schema(request=MemberSerializer, responses=MemberSerializer)
@api_view(['GET'])
# @permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_DETAILS.name])
def getAMember(request, pk):
	try:
		member = Member.objects.get(pk=pk)
		serializer = MemberSerializer(member)
		return Response(serializer.data, status=status.HTTP_200_OK)
	except ObjectDoesNotExist:
		return Response({'detail': f"Member id - {pk} does't exists"}, status=status.HTTP_400_BAD_REQUEST)




@extend_schema(request=MemberSerializer, responses=MemberSerializer)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.PERMISSION_DETAILS_VIEW.name])
def searchMember(request):
	keyword = request.query_params.get('keyword')
	members = Member.objects.filter(Q(username__icontains=keyword) | Q(email__icontains=keyword))

	print('searched_menbers: ', members)

	total_elements = members.count()

	page = request.query_params.get('page')
	size = request.query_params.get('size')

	# Pagination
	pagination = Pagination()
	pagination.page = page
	pagination.size = size
	members = pagination.paginate_data(members)

	serializer = MemberListSerializer(members, many=True)

	response = {
		'members': serializer.data,
		'page': pagination.page,
		'size': pagination.size,
		'total_pages': pagination.total_pages,
		'total_elements': total_elements,
	}

	if len(members) > 0:
		return Response(response, status=status.HTTP_200_OK)
	else:
		return Response({'detail': f"There are no members matching your search"}, status=status.HTTP_204_NO_CONTENT)


@extend_schema(request=MemberSerializer, responses=MemberSerializer)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_CREATE.name])
def createMember(request):
	data = request.data
	print('data: ', data)
	print('content_type: ', request.content_type)
	filtered_data = {}
	for key, value in data.items():
		if value != '' and value != 0 and value != '0':
			filtered_data[key] = value

	filtered_data['last_login'] = timezone.now()
	filtered_data['user_type'] = 'member'
	print('filtered_data: ', filtered_data)
	serializer = MemberSerializer(data=filtered_data)
	if serializer.is_valid():
		serializer.save()
		# group_obj = Group.objects.get(name='Sundry Creditors')
		# id = serializer.data['id']
		# username = serializer.data['username']
		# LedgerAccount.objects.create(name=username, reference_id=id, ledger_type='member_ledger', head_group=group_obj)
		return Response(serializer.data, status=status.HTTP_201_CREATED)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=MemberSerializer, responses=MemberSerializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_UPDATE.name])
def updateMember(request, pk):
	data = request.data
	print('data :', data)
	filtered_data = {}

	try:
		member_obj = Member.objects.get(pk=pk)
	except ObjectDoesNotExist:
		return Response({'detail': f"Product id - {pk} doesn't exists"})

	for key, value in data.items():
		if value != '' and value != '0':
			filtered_data[key] = value

	print('filtered_data: ', filtered_data)
		
	image = filtered_data.get('image', None)
	favicon = filtered_data.get('favicon', None)

	if image is not None and type(image) == str:
		image = filtered_data.pop('image')

	serializer = MemberSerializer(member_obj, data=filtered_data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data, status=status.HTTP_200_OK)
	else:
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=MemberSerializer, responses=MemberSerializer)
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
# @has_permissions([PermissionEnum.ATTRIBUTE_DELETE.name])
def deleteMember(request, pk):
	try:
		member = Member.objects.get(pk=pk)
		member.delete()
		return Response({'detail': f'Member id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
	except ObjectDoesNotExist:
		return Response({'detail': f"Member id - {pk} does't exists"}, status=status.HTTP_400_BAD_REQUEST)



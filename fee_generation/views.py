from django.shortcuts import render


from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from commons.pagination import Pagination
from fee_generation.models import FeeGeneration
from fee_generation.serializers import FeeGenerationSerializer


@extend_schema(
    parameters=[
        OpenApiParameter("page"),
        OpenApiParameter("size"),
    ],
    request=FeeGenerationSerializer,
    responses=FeeGenerationSerializer
)
@api_view(['GET'])
def getAllFeeGeneration(request):

    fee_generation = FeeGeneration.objects.all()
    total_elements = fee_generation.count()

    page = request.query_params.get('page')
    size = request.query_params.get('size')

    # Pagination
    pagination = Pagination()
    pagination.page = page
    pagination.size = size
    fee_generation = pagination.paginate_data(fee_generation)

    serializer = FeeGenerationSerializer(fee_generation, many=True)

    response = {
        'fee_generation': serializer.data,
        'page': pagination.page,
        'size': pagination.size,
        'total_pages': pagination.total_pages,
        'total_elements': total_elements,
    }
    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=FeeGenerationSerializer, responses=FeeGenerationSerializer)
@api_view(['GET'])
def getAFeeGenerator(request, pk):

    try:
        fee_generation = FeeGeneration.objects.get(pk=pk)
        serializer = FeeGenerationSerializer(fee_generation)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f"getAFeeGenerator id - {pk} does't exists"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=FeeGenerationSerializer, responses=FeeGenerationSerializer)
@api_view(['POST'])
def createFeeGeneration(request):

    data = request.data
    print('data: ', data)
    print('content_type: ', request.content_type)
    filtered_data = {}
    for key, value in data.items():
        if value != '' and value != 0 and value != '0':
            filtered_data[key] = value

    print('filtered_data: ', filtered_data)
    serializer = FeeGenerationSerializer(data=filtered_data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=FeeGenerationSerializer, responses=FeeGenerationSerializer)
@api_view(['PUT'])
def updateFeeGenerator(request, pk):
    data = request.data
    print('data :', data)
    filtered_data = {}

    try:
        fee_generation = FeeGeneration.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'detail': f"FeeGenerator id - {pk} doesn't exists"})

    for key, value in data.items():
        if value != '' and value != '0':
            filtered_data[key] = value

    print('filtered_data: ', filtered_data)
    serializer = FeeGenerationSerializer(fee_generation, data=filtered_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)


@extend_schema(request=FeeGenerationSerializer, responses=FeeGenerationSerializer)
@api_view(['DELETE'])
def deleteFeeGenerator(request, pk):

    try:
        fee_generation = FeeGeneration.objects.get(pk=pk)
        fee_generation.delete()
        return Response({'detail': f'fee_generation id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'detail': f"fee_generation id - {pk} does't exists"}, status=status.HTTP_400_BAD_REQUEST)

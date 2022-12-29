from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from commons.pagination import Pagination
from department.models import department
from department.serializers import DepartmentSerializers


# Create your views here.


@extend_schema(
    parameters=[
        OpenApiParameter("page"),
        OpenApiParameter("size")
    ],
    request=DepartmentSerializers,
    responses=DepartmentSerializers
)
@api_view(["GET"])
def getAlldepartment(request):
    departments = department.objects.all()
    total_elements = departments.count()
    serializer = DepartmentSerializers(departments, many=True)
    page = departments.query_params.get('page'),
    size = departments.query_params.get('size'),

    # Pagination Part

    pagination = Pagination(),
    pagination.page = page,
    pagination.size = size,
    department_pagination = pagination.paginate_data(department)
    response = {
        "departments": serializer.data,
        "total_elements": total_elements,
        "pages": page,
        "size": size,
        "total_page": department_pagination.total_pages
    }
    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=DepartmentSerializers, responses=DepartmentSerializers)
@api_view(["GET"])
def getADepartment(request, pk):
    try:
        a_department = department.objects.get(pk=pk)
        serializer = DepartmentSerializers(a_department)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({"details": f"department Id  {pk} doesnt exist"}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=DepartmentSerializers, responses=DepartmentSerializers)
@api_view(['POST'])
def createDepartment(request):
    data = request.data
    print('data:', data)
    print('content_type:', request.content_type)
    filterd_data = {}
    for key, value in data.items():
        if value != '' and value != '0' and value != 0:
            filterd_data[key] = value
    print('filterd_data:', filterd_data)
    serializer = DepartmentSerializers(data=filterd_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=DepartmentSerializers, responses=DepartmentSerializers)
@api_view(['PUT'])
def updateDepartment(request, pk):

    data = request.data
    print('data:', data)
    filterd_data = {}
    for key, value in data.items():
        if value != '0' and value != 0 and value != '':
            filterd_data[key] = value
    try:
        departments = department.objects.get(pk=pk)
    except ObjectDoesNotExist:
        return Response({'details:' f'department id {pk} doesnt match'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = DepartmentSerializers(departments, data=filterd_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors)


@extend_schema(request=DepartmentSerializers, responses=DepartmentSerializers)
@api_view(['DELETE'])
def deleteDepartment(request, pk):
    try:
        departments = department.objects.get(pk=pk)
        departments.delete()
        return Response({'detail': f'department id - {pk} is deleted successfully'}, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'details': f'department doesnt exist'}, status=status.HTTP_400_BAD_REQUEST)

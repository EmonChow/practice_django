from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from commons.pagination import Pagination
from schedule.models import Schedule
from schedule.serializer import ScheduleSerializer


# Create your views here.

@extend_schema(parameters=[
    OpenApiParameter("page"),
    OpenApiParameter("size")
],
    request=ScheduleSerializer,
    responses=ScheduleSerializer
)
@api_view(["GET"])
def allSchedule(request):
    schedules = Schedule.objects.all()
    total_elements = schedules.count()
    serializer = ScheduleSerializer(schedules, many=True)
    page = schedules.query_params.get("page")
    size = schedules.query_params.get("size")

    #     Pagination
    pagination = Pagination()
    pagination.page = page
    pagination.size = size
    schedule_pagination = pagination.paginate_data(schedules)
    response = {
        "schedules": serializer.data,
        "total_elements": total_elements,
        "schedule_pagination": schedule_pagination,
        "page": page,
        "size": size
    }
    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=ScheduleSerializer, responses=ScheduleSerializer)
@api_view(['POST'])
def create_Schedule(request):
    data = request.data
    print('data:', data)
    print('content_type:', request.content_type)
    filterd_data = {}
    for key, value in data.items():
        if value != '' and value != '0' and value != 0:
            filterd_data[key] = value
    print('filterd_data:', filterd_data)
    serializer = ScheduleSerializer(data=filterd_data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=ScheduleSerializer, responses=ScheduleSerializer)
@api_view(['GET'])
def getASchedule(request, pk):
    try:
        schedule = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response({'details:' f'schedule id {pk} does not exist'}, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(request=ScheduleSerializer, responses=ScheduleSerializer)
@api_view(["PUT"])
def updateSchedule(request, pk):
    data = request.data
    print('data:', data)
    filterd_data = {}
    for key, value in data.items():
        if value != 0 and value != '' and value != '0':
            filterd_data[key] = value
    try:
        schedule = Schedule.objects.get(pk=pk)
        serializer = ScheduleSerializer(schedule)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response('details:' f'schedule id {pk} does not exist')

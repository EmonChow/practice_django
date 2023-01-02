from django.core.exceptions import ObjectDoesNotExist
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from commons.pagination import Pagination
from schedule.models import ScheduleDay
from schedule.serializer import ScheduleDaysSerializer


@extend_schema(parameters=[
    OpenApiParameter("page"),
    OpenApiParameter("size")
])
@api_view(['GET'])
def ScheduleDays(request):
    schedules_day = ScheduleDay.objects.all()
    total_elements = schedules_day.count()

    page = request.query_params.get('page')
    size = request.query_params.get('size')

    pagination = Pagination()
    pagination.page = page
    pagination.size = size
    schedule_day_pagination = pagination.paginate_data(schedules_day)
    serializer = ScheduleDaysSerializer(schedule_day_pagination)
    response = {
        'schedule_days': serializer.data,
        'total_element': total_elements,
        'total_page': schedule_day_pagination,
    }
    return Response(response, status=status.HTTP_200_OK)


@extend_schema(request=ScheduleDaysSerializer, responses=ScheduleDaysSerializer)
@api_view(['POST'])
def createScheduleDay(request):
    data = request.data
    print('data:', data)
    print('content_type:', request.content_type)
    filterd_data = {}
    for key, value in data.items():
        if value != 0 and value != '' and value != '0':
            filterd_data[key] = value
    print('filterd_data:', filterd_data)
    serializer = ScheduleDaysSerializer(data=filterd_data)
    if serializer.is_valid():
        return Response(serializer.data)
    else:
        return Response(serializer.errors)


@extend_schema(request=ScheduleDaysSerializer, responses=ScheduleDaysSerializer)
@api_view(['GET'])
def getAScheduleDay(request, pk):
    try:
        schedule_day = ScheduleDay.objects.get(pk=pk)
        serializer = ScheduleDaysSerializer(schedule_day)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response('details:' f'schedule day id {pk} does not exist')


@extend_schema(request=ScheduleDaysSerializer, responses=ScheduleDaysSerializer)
@api_view(['PUT'])
def updateScheduleDay(request, pk):
    data = request.data
    print('data:', data)
    filterd_data = {}
    for key, value in data.items():
        if value != 0 and value != '' and value != '0':
            filterd_data[key] = value
    try:
        schedule_day = ScheduleDay.objects.get(pk=pk)
        serializer = ScheduleDaysSerializer(schedule_day)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except ObjectDoesNotExist:
        return Response('details:' f'schedule day id {pk} does not exist')


@extend_schema(request=ScheduleDaysSerializer, responses=ScheduleDaysSerializer)
@api_view(['DELETE'])
def deleteScheduleday(request, pk):
    try:
        schedule_day = ScheduleDay.objects.get(pk=pk)
        schedule_day.delete()
        return Response('details:'f'schedule day id {pk} deleted successfully')
    except ObjectDoesNotExist:
        return Response('details:'f'id does not exist')

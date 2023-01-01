from django.urls import path

from schedule.views import schedule_day_views

urlpatterns = [
    path('api/schedule_days', schedule_day_views.ScheduleDays),
    path('api/schedule_create', schedule_day_views.createScheduleDay),
    path('api/a_schedule/<int:pk>', schedule_day_views.getAScheduleDay),
    path('api/update_schedule_day/<int:pk>', schedule_day_views.updateScheduleDay),
    path('api/delete_schedule_day/<int:pk>', schedule_day_views.deleteScheduleday)
]



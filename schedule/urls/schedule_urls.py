from django.urls import path

from schedule.views import schedule_views

urlpatterns = [
    path('api/schedules/', schedule_views.allSchedule),
    path('api/create_schedule/', schedule_views.create_Schedule),
    path('api/get_a_schedule/<int:pk>', schedule_views.getASchedule),
    path('api/update_schedule/<int:pk>', schedule_views.updateSchedule)
]
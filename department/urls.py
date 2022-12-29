from django.urls import path
from department import views


urlpatterns = [
    path('api/v1/department/all/', views.getAlldepartment),
    path('api/v1/get_a_department/<int:pk>', views.getADepartment),
    path('api/v1/create_department/', views.createDepartment),
    path('api/v1/update_department/<int:pk>', views.updateDepartment),
    path('api/v1/delete_department/<int:pk>', views.deleteDepartment),

]
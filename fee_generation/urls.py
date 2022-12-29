from django.urls import path
from fee_generation import views


urlpatterns = [
    path('api/v1/fee_generation/all/', views.getAllFeeGeneration),
    path('api/v1/fee_generation/get_a_fee_generator/<int:pk>', views.getAFeeGenerator),
    path('api/v1/fee_generation/create_fee_generator/', views.createFeeGeneration),
    path('api/v1/fee_generation/update_fee_generator/<int:pk>', views.updateFeeGenerator),
    path('api/v1/fee_generation/delete_fee_generator/<int:pk>', views.deleteFeeGenerator),

]
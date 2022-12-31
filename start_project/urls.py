"""start_project URL Configuration."""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView)

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index),

    # Authentication module
    path('user/', include('authentication.urls.user_urls')),
    path('employee/', include('authentication.urls.employee_urls')),
    path('vendor/', include('authentication.urls.vendor_urls')),
    path('customer_type/', include('authentication.urls.customer_type_urls')),
    path('customer/', include('authentication.urls.customer_urls')),
    path('permission/', include('authentication.urls.permission_urls')),
    path('role/', include('authentication.urls.role_urls')),
    path('designation/', include('authentication.urls.designation_urls')),
    path('department/', include('authentication.urls.department_urls')),
    path('qualification/', include('authentication.urls.qualification_urls')),

    path('country/', include('authentication.urls.country_urls')),
    path('thana/', include('authentication.urls.thana_urls')),
    path('area/', include('authentication.urls.area_urls')),
    path('branch/', include('authentication.urls.branch_urls')),
    path('city/', include('authentication.urls.city_urls')),

    # Account Module
    path('primary_group/', include('account.urls.primary_group_urls')),
    path('group/', include('account.urls.group_urls')),
    path('ledger_account/', include('account.urls.ledger_account_urls')),
    path('sub_ledger_account/', include('account.urls.sub_ledger_account_urls')),
    path('payment_voucher/', include('account.urls.payment_voucher_urls')),
    path('receipt_voucher/', include('account.urls.receipt_voucher_urls')),
    path('sales/', include('account.urls.sales_urls')),
    path('purchase/', include('account.urls.purchase_urls')),
    path('contra/', include('account.urls.contra_urls')),
    path('journal/', include('account.urls.journal_urls')),
    path('idjournal/', include('account.urls.idjournal_urls')),
    path('account_log/', include('account.urls.account_log_urls')),

    # Account Statement
    path('account_log_report/', include('account.urls.account_log_report_urls')),
    path('account_report/', include('account.urls.account_report_urls')),

    # Balance Sheet
    path('balance_sheet/', include('account.urls.balance_sheet_urls')),

    # CMS
    path('cms_menu/', include('cms.urls.cms_menu_urls')),
    path('cms_menu_content/', include('cms.urls.cms_menu_content_urls')),
    path('cms_menu_content_image/', include('cms.urls.cms_menu_content_image_urls')),

    # Donation
    path('cause/', include('donation.urls.cause_urls')),
    path('cause_content/', include('donation.urls.cause_content_urls')),
    path('cause_content_image/', include('donation.urls.cause_content_image_urls')),
    path('payment_method/', include('donation.urls.payment_method_urls')),
    path('payment_method_detail/', include('donation.urls.payment_method_detail_urls')),
    path('donation/', include('donation.urls.donation_urls')),
    path('cause_donation/', include('donation.urls.cause_donation_urls')),
    path('monthly_subscription/', include('donation.urls.monthly_subscription_urls')),

    # Support module
    path('member/', include('member.urls.member_urls')),
    path('executive_member/', include('member.urls.executive_member_urls')),
    path('adviser_member/', include('member.urls.adviser_member_urls')),
    path('general_member/', include('member.urls.general_member_urls')),

    # Fee Generation Module
    # path('member_fee_generation/', include('member.urls.fee_generation_urls')),
    path('fee_generation/', include('fee_generation.urls')),
    path('department/', include('department.urls')),
    path('schedule/', include('schedule.urls.schedule_urls')),
    path('schedule_day/', include('schedule.urls.schedule_day_urls')),

    # Support module
    path('ticket_department/', include('support.urls.ticket_department_urls')),
    path('ticket_priority/', include('support.urls.ticket_priority_urls')),
    path('ticket_status/', include('support.urls.ticket_status_urls')),
    path('ticket/', include('support.urls.ticket_urls')),
    path('ticket_detail/', include('support.urls.ticket_detail_urls')),

    path('message/', include('support.urls.message_urls')),

    path('task_type/', include('support.urls.task_type_urls')),
    path('todo_task/', include('support.urls.todo_task_urls')),

    # YOUR PATTERNS
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    path('djoser/auth/', include('djoser.urls')),
    path('djoser/auth/', include('djoser.urls.jwt')),

    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

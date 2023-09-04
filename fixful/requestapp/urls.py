from django.urls import re_path
from fixful.requestapp import views as request_views

urlpatterns = [
    
    re_path(r'^request_form/', request_views.request_form_view , name='request_form'),
    re_path(r'^display_request_details/', request_views.display_request_details , name='display_request_details'),
    re_path(r'^view_fix_detail/(?P<req_id>\d+)', request_views.fixDetails , name='view_fix_detail'),
    re_path(r'^accept_fix/(?P<req_id>\d+)', request_views.acceptFix, name='accept_fix'),
    re_path(r'^active_logs/', request_views.activeLogs , name='active_logs'),
    re_path(r'^finish_logs/', request_views.finishLogs , name='finish_logs'),
]
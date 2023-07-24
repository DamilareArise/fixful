from django.urls import re_path
from fixful.requestapp import views as request_views

urlpatterns = [
    
    re_path(r'^request_form/', request_views.request_form_view , name='request_form'),
    re_path(r'^my_request/', request_views.display_request_details , name='display_request_details'),
    re_path(r'^request_service/(?P<req_id>\d+)', request_views.approveRequest , name='request_service'),


]
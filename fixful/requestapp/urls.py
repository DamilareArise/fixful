from django.urls import re_path
from fixful.requestapp import views as request_views

urlpatterns = [
    
    re_path(r'^request_form/', request_views.request_form_view , name='request_form'),

]
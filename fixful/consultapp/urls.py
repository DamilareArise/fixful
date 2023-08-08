from django.urls import re_path
from fixful.consultapp import views as consult_views

urlpatterns = [
    re_path(r'^consultation_form/', consult_views.consultation_form_view , name='consultation_form'),
    re_path(r'^consultation/', consult_views.display_consult_view , name='display_consult'),
    # re_path(r'^assign_staff/', consult_views.assignStaff , name='display_consult'),

]
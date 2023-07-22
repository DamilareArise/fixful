from django.urls import re_path, path
from fixful.userapp import views as user_views

urlpatterns = [
    
    re_path(r'^profile/(?P<userid>\d+)/',user_views.profile, name='profile'),
    re_path(r'^edit_user_profile/(?P<userid>\d+)/',user_views.editUserProfile, name='edit_user_profile'),
    re_path(r'^edit_admin_profile/(?P<userid>\d+)/',user_views.editAdminProfile, name='edit_admin_profile'),
    re_path(r'^deactivate_profile/(?P<userid>\d+)/',user_views.deactivateProfile, name='deactivate_profile'),
    re_path(r'^show_user/(?P<user>\D+)/',user_views.displayUsers, name='show_user'),
    re_path(r'^dashboard/',user_views.dashboard, name='dashboard'),
]
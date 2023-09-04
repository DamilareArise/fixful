from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic
from .forms import SignUpForm, User_update_form, Admin_update_form, User_form
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponsePermanentRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime as dt

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url  = reverse_lazy("login")
    template_name = 'registration/signup.html'

@login_required
def profile(request, userid):
    user_profile = Profile.objects.all().filter(user_id = userid)
    return render(request, "userApp/user_profile.html", {"userprofile":user_profile})

@login_required
def editAdminProfile(request, userid):
    if request.method == "POST":
        user = get_object_or_404(User, id=userid)
        user_form = User_form(request.POST, instance=user)
        profile_form = Admin_update_form(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
                
            user_form.save()
            profile_form.save()
            if profile_form.cleaned_data['staff']:
                user.is_staff = True
                user.save()
            else:
                user.is_staff = False
                user.save()

            print("valid valid")
            user.save()
            messages.success(request, 'Your profile was successfully updated!')
            return profile(request, userid)
        else:
            print("invalid invalid")
            messages.error(request, 'Please correct the error below.')
            return HttpResponsePermanentRedirect(reverse('edit_admin_profile', args=(userid,)))
    
    else:
        user = get_object_or_404(User, id=userid)
        user_form = User_form(instance=user)
        profile_form = Admin_update_form(instance=user.profile)
        return render(request, 'userapp/edit_profile_form.html', {'user_form': user_form, 'profile_form': profile_form})

@login_required
def editUserProfile(request, userid):
    if request.method == "POST":
        user = get_object_or_404(User, id=userid)
        user_form = User_form(request.POST, instance=user)
        profile_form = User_update_form(request.POST, request.FILES, instance=user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return profile(request, userid)
        else:
            messages.error(request, 'Please correct the error below.')
            return HttpResponsePermanentRedirect(reverse('edit_user_profile', args=(userid,)))
    else:
        user = get_object_or_404(User, id=userid)
        user_form = User_form(instance=user)
        profile_form = User_update_form(instance=user.profile)
        return render(request, 'userapp/edit_profile_form.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required   
def deactivateProfile(request, userid):
    myprofile = User.objects.get(id=userid)
    if myprofile.is_active == True:
        User.objects.only("is_active").filter(id=userid).update(is_active=False)
        Profile.objects.only("status").filter(user_id=userid).update(status="Suspended")

    else:
        User.objects.only("is_active").filter(id=userid).update(is_active=True)
        Profile.objects.only("status").filter(user_id=userid).update(status="Active")


    return HttpResponsePermanentRedirect(reverse("profile",args=(userid,)))

@login_required
def displayUsers(request, user):

    if user == "staff":
        allUser = User.objects.all().filter(is_staff=True)
        
    else:
        allUser = User.objects.all().filter(is_staff=False)


    return render(request, "userapp/display_user.html",  {"allUser":allUser, "status":user})


def dashboard(request):
    datetime_now = dt.datetime.now()
    print(datetime_now)

    return render(request, "userapp/dashboard.html", {'date':datetime_now})
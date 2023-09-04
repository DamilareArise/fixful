from django.shortcuts import render, redirect, get_object_or_404
from .models import Repair_category
from .forms import AcceptFix_forms, Request_form
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.http import HttpResponsePermanentRedirect, HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
from django.contrib import messages
from fixful.userapp.models import Profile

@login_required
def request_form_view(request):
    datetime_now = dt.datetime.now()
    if request.method == 'POST':
        request_formA = Request_form(request.POST)
        if request_formA.is_valid():
            print("valid")
            form = request_formA.save(commit=False)
            form.user_id= request.user.id
            
            agent = Profile.objects.filter(position = 'Consultant').values()
            agent_id = random.randint(0, len(agent)-1)
            service_agent = agent[agent_id]
            print(service_agent)

            staff_id = service_agent.get("user_id")
            instance = User.objects.get(id = staff_id)

            form.staff_in_charge = instance
            form.save()

            email = service_agent.get("email")
            send_mail(
                'Fix Alert',# Subject of the mail
                'A customer just asked for a Fix. Kindly login and do a proper follow up', # Body of the mail
                'support@fixtul.com', # From email (Sender)
                [email], # To email (Receiver)
                fail_silently=False, # Handle any error
            )

            user = User.objects.filter(id=request.user.id).values()
            user_email = user[0]['email']
            firstname = user[0]['first_name']
            lastname = user[0]['last_name']
            
            send_mail(
                'Fix Consult',# Subject of the mail
                f'Thank You {firstname} {lastname}, your fix request has been recieved and would be attended to shortly.', # Body of the mail
                'support@fixtul.com', # From email (Sender)
                [user_email], # To email (Receiver)
                fail_silently=False, # Handle any error
            )
            messages.success(request, 'Request Sent Successfully')
            return HttpResponseRedirect('request_form')
        else:
            messages.error(request, 'Request not sent. Fill the above form correctly')
            return HttpResponseRedirect('request_form')
    else:
        form = Request_form()
    
    return render(request, 'requestapp/request.html', {'form': form, 'date':datetime_now})

@login_required
def display_request_details(request):
    user_staff = request.user.is_staff
    datetime_now = dt.datetime.now()
    if user_staff == 1:
        user_requests = Repair_category.objects.filter(status='Pending').order_by('date_created').reverse()

        return render(request, 'requestapp/display_request_details.html', {'user_requests': user_requests, 'date':datetime_now})

    else:
        user_requests = Repair_category.objects.filter(user_id=request.user.id).order_by('date_created').reverse()
        return render(request, 'requestapp/display_request_details.html', {'user_requests': user_requests, 'date':datetime_now})

@login_required
def activeLogs(request):
    datetime_now = dt.datetime.now()
    user_requests = Repair_category.objects.filter(status='Active').order_by('date_created').reverse()
    return render(request, 'requestapp/display_request_details.html', {'user_requests': user_requests, 'date':datetime_now})

@login_required
def finishLogs(request):
    datetime_now = dt.datetime.now()
    user_requests = Repair_category.objects.filter(status='Finished').order_by('date_created').reverse()
    return render(request, 'requestapp/display_request_details.html', {'user_requests': user_requests, 'date':datetime_now})


@login_required
def fixDetails(request, req_id):
    my_fix = Repair_category.objects.filter(service_id = req_id)
    return render (request, 'requestapp/view_fix.html', {'my_fix':my_fix})


@login_required
def acceptFix(request, req_id):
    if request.method == 'POST':
        fix= get_object_or_404(Repair_category, service_id = req_id)
        fix_form = AcceptFix_forms(request.POST, instance=fix)
        if fix_form.is_valid():
            fix_form.save()
  
            #send mail notification to client
            
            status = fix.status
      
            if status == 'Active':
                send_mail(
                'Fix Active',
                f'Dear {fix.user.first_name}, Your fix request is active. see your fix details for more information or click <a href= "fixtul.com/requestapp/view_fix/{fix.user_id}">Booking details</a>.\n Thanks. \n http://127.0.0.1:8000/requestapp/view_fix/{fix.user_id} ',
                'support@fixtul.com',
                [fix.user.email],
                fail_silently=False,
            )
                
            elif status == 'Finished': 
                send_mail(
                'Fix Finished',
                f'Dear {fix.user.first_name}, Your Device has been fully Fixed. see your fix details for more information or click <a href= "fixtul.com/requestapp/view_fix/{fix.user_id}">Booking details</a>.\n Thanks. \n http://127.0.0.1:8000/requestapp/view_fix/{fix.user_id} ',
                'support@fixtul.com',
                [fix.user.email],
                fail_silently=False,
            )
            
            else:
                send_mail(
                'Fix Pending',
                f'Dear {fix.user.first_name}, Your fix request is pending. see your fix details for more information or click <a href= "fixtul.com/requestapp/view_fix/{fix.user_id}">Booking details</a>.\n Thanks. \n http://127.0.0.1:8000/requestapp/view_fix/{fix.user_id} ',
                'support@fixtul.com',
                [fix.user.email],
                fail_silently=False,
            )
            messages.success(request, ('Fix edited successfully'))
            return HttpResponsePermanentRedirect(reverse('view_fix_detail', args=(req_id,)))
        else:
            messages.error(request, ('Please correct the error below'))
            return HttpResponsePermanentRedirect(reverse('accept_fix', args=(req_id,)))
        
    else:
        fix= get_object_or_404(Repair_category, service_id = req_id)
        fix_form = AcceptFix_forms(request.POST, instance=fix)
        return render (request, 'requestapp/edit_fix_detail.html', {'fix_form':fix_form})
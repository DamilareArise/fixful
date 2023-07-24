from django.shortcuts import render, redirect
from .forms import Request_form
from .models import Repair_category
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random

@login_required
def request_form_view(request):
    datetime_now = dt.datetime.now()
    if request.method == 'POST':
        request_formA = Request_form(request.POST)
        if request_formA.is_valid():
            print("valid")
            form = request_formA.save(commit=False)
            form.user_id= request.user.id
            
            agent = User.objects.filter(is_superuser=True).values()
            print(len(agent))
            agent_id = random.randint(0, len(agent)-1)
            print(agent_id)
            service_agent = agent[agent_id]
            form.save()


            email = service_agent.get("email")
            send_mail(
                'Fix Alert',# Subject of the mail
                'A customer just asked for a Fix. Kindly login and do a proper follow up', # Body of the mail
                'sunday@gmail.com', # From email (Sender)
                [email], # To email (Receiver)
                fail_silently=False, # Handle any error
            )

            return HttpResponsePermanentRedirect(reverse('request_form'))
        else:
            print("not valid")
            return HttpResponsePermanentRedirect(reverse('request_form'))

    else:
        form = Request_form()
    
    return render(request, 'requestapp/request.html', {'form': form, 'date':datetime_now})

@login_required
def display_request_details(request):
    user_staff = request.user.is_staff
    datetime_now = dt.datetime.now()
    if user_staff == 1:
        user_requests = Repair_category.objects.all()
        return render(request, 'requestapp/display_request_details.html', {'user_requests': user_requests, 'date':datetime_now })
    else:
        user_requests = Repair_category.objects.filter(user_id=request.user.id)
        return render(request, 'requestapp/display_request_details.html', {'user_requests': user_requests, 'date':datetime_now })

@login_required
def approveRequest(request, req_id):
    user_superuser = request.user.is_superuser
    if user_superuser == 1:
        approve = Repair_category.objects.get(service_id=req_id)
        if approve.status == True:
            Repair_category.objects.filter(service_id=req_id).update(status=False)
        else:
            Repair_category.objects.filter(service_id=req_id).update(status=True)
        return display_request_details(request)
    else:
        return display_request_details(request) 

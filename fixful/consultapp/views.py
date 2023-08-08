from django.shortcuts import render
from .forms import consultation_form
from .models import Consult
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.models import User
import random
from django.contrib import messages


# Create your views here.


@login_required
def consultation_form_view(request):
    datetime_now = dt.datetime.now()
    if request.method == 'POST':
        consultant_form = consultation_form(request.POST)
        if consultant_form.is_valid():
            print("valid")
            form_consult = consultant_form.save(commit=False)
            form_consult.user_id= request.user.id
            
            agent = User.objects.filter(is_superuser=True).values()
            print(len(agent))
            agent_id = random.randint(0, len(agent)-1)
            print(agent_id)
            service_agent = agent[agent_id]
            form_consult.save()


            email = service_agent.get("email")
            send_mail(
                'Fix Consult',# Subject of the mail
                'A customer just sent a complain concerning a Fix. Kindly login and do a proper follow up', # Body of the mail
                'Fixtul@gmail.com', # From email (Sender)
                [email], # To email (Receiver)
                fail_silently=False, # Handle any error
            )
            user = User.objects.filter(id=request.user.id).values()
            user_email = user[0]['email']
            firstname = user[0]['first_name']
            lastname = user[0]['last_name']
            
            send_mail(
                'Fix Consult',# Subject of the mail
                f'Thank You {firstname} {lastname}, your complain has been recieved and would be attended to shortly.', # Body of the mail
                'Fixtul@gmail.com', # From email (Sender)
                [user_email], # To email (Receiver)
                fail_silently=False, # Handle any error
            )

            messages.success(request, 'Complain sent Successfully')
            return HttpResponsePermanentRedirect(reverse('consultation_form'))
        else:
            print("not valid")
            return HttpResponsePermanentRedirect(reverse('consultation_form'))

    else:
        form_consult = consultation_form()
    
    return render(request, 'consultapp/support.html', {'form_consult': form_consult, 'date':datetime_now})



@login_required
def display_consult_view(request):
    user_staff = request.user.is_staff
    datetime_now = dt.datetime.now()
    
    if user_staff == 1:
        user_consult = Consult.objects.all()
    
        return render(request, 'consultapp/display_consult.html', {'user_consult': user_consult, 'date':datetime_now})
    
# @login_required
# def assign_staff(request):
#     agent = User.objects.filter(is_staff=True).values()
#     staffs = agent.get("id")
#     if request.method == 'POST':
#         consultant_form = assign_staff_form(request.POST)
#         if consultant_form.is_valid():
#             pass

    
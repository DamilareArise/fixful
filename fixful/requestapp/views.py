from django.shortcuts import render, redirect
from .forms import Request_form
from django.contrib.auth.decorators import login_required
import datetime as dt
from django.http import HttpResponsePermanentRedirect
from django.urls import reverse

@login_required
def request_form_view(request):
    datetime_now = dt.datetime.now()
    if request.method == 'POST':
        request_formA = Request_form(request.POST)
        if request_formA.is_valid():
            print("valid")
            form = request_formA.save(commit=False)
            form.user_id= request.user.id
            form.save()
            return HttpResponsePermanentRedirect(reverse('request_form'))
        else:
            print("not valid")
            return HttpResponsePermanentRedirect(reverse('request_form'))

    else:
        form = Request_form()
    
    return render(request, 'requestapp/request.html', {'form': form, 'date':datetime_now})


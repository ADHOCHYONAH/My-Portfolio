from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
import datetime
from .models import PORTFOLIOITEM
from .form import FORM
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import context
from .form import FORM


# Create your views here.
# def adhoch(request):
# now = datetime.datetime.now()
# html = "Time is {}".format(now)

# return HttpResponse(html)

def homepage(request):
    return render(request, 'index.html', {'title': 'homepage'})


def list_view(request):
    pin = PORTFOLIOITEM.objects.all()
    return render(request, 'About.html', {'pin': pin})


def portfolio(request):

    return render(request, 'Portfolio.html', {})


def register(request):
    if request.method == 'POST':
        form = FORM(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registration_success')
    else:
        form = FORM()
        return render(request, 'register.html', {'form': form})



def Login(request):
    if request.method == 'POST':

        # AuthenticationForm_can_also_be_used__

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            messages.success(request, f' welcome {username} !!')
            return redirect('index')
        else:
            messages.info(request, f'account done not exit plz sign in')
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form, 'title': 'log in'})

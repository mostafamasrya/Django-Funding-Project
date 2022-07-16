from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.utils import timezone
from .forms import *
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
import re
import datetime
from projects.models import Usercrowd


# Create your views here.


def register_user(request):
    if request.method == 'POST':

        name_regex = r"^[a-zA-Z ,.'-]+$"
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        phone_regex = r'^01[0125][0-9]{8}$'
        if (re.search(name_regex, request.POST['first_name']) == None):
            context = {}
            context['errorfname'] = 'This First Name Is Not Valid Enter Valid Name'
            return render(request, 'register.html', context)
        if (re.search(name_regex, request.POST['last_name']) == None):
            context = {}
            context['errorlname'] = 'This Last Name Is Not Valid Enter Valid Name'
            return render(request, 'register.html', context)
        if (re.search(email_regex, request.POST['email']) == None):
            context = {}
            context['erroremail'] = 'This Email Is Not Valid Enter Valid Email'
            return render(request, 'register.html', context)
        if (re.search(phone_regex, request.POST['phone_number']) == None):
            context = {}
            context[
                'errorphone'] = 'Phone number must be entered in the format: "01[0125][0-9]{8}". Exactly 11 digits allowed.'
            return render(request, 'register.html', context)
        if (request.POST['password'] == request.POST['repassword']):
            newuser = Usercrowd.objects.create(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                email=request.POST['email'], password=request.POST['password'],
                phone_number=request.POST['phone_number'], profile_img=request.FILES['profile_img'],
                expire_date=datetime.datetime.now() + datetime.timedelta(days=1), birthdate=request.POST['birthdate'],
                country=request.POST['country'], facebooklink=request.POST['facebooklink']
            )
            htmly = get_template('Welcome.html')
            context = {}
            context['username'] = request.POST['first_name']
            context['id'] = newuser.id

            subject, from_email, to = 'welcome to crowd funding world', settings.EMAIL_HOST_USER, request.POST['email']
            html_content = htmly.render(context)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return render(request, 'successregister.html')
        else:
            context = {}
            context['notequal'] = 'Password And Repeat Password Not Equal'
            return render(request, 'register.html', context)
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        loguser = Usercrowd.objects.filter(email=request.POST['email'], password=request.POST['password'])

        if len(loguser) > 0:
            if (loguser[0].is_active == True):
                request.session['user_name'] = loguser[0].first_name + " " + loguser[0].last_name
                request.session['user_id'] = loguser[0].id
                return redirect('home')

            else:
                return render(request, 'notactiveerror.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid Credientials'})
    else:
        return render(request, 'login.html')


def activeEmail(request, id):
    loguser = Usercrowd.objects.filter(id=id)
    if len(loguser) > 0 and loguser[0].is_active == False:
        expire_day = loguser[0].expire_date
        daynow = timezone.now()
        if expire_day > daynow:
            Usercrowd.objects.filter(id=id).update(is_active=True)
            return redirect('login')
        else:
            Usercrowd.objects.filter(id=id).delete()
            return render(request, 'expirederror.html')
    else:
        return render(request, 'notfounderror.html')


def logout(request):
    if request.session.has_key('user_name'):
        del request.session['user_name']
        del request.session['user_id']
        return redirect('login')
    return redirect('login')


def profile(request):
    if request.session.has_key('user_name'):
        user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
        # context = {}
        # context['imgname'] = user.profile_img
        return render(request, 'profile.html', {'user': user})
    else:
        return redirect('login')


def editProfile(request):
    if request.session.has_key('user_name'):
        if request.method == 'POST':
            name_regex = r"^[a-zA-Z ,.'-]+$"
            phone_regex = r'^01[0125][0-9]{8}$'
            if (re.search(name_regex, request.POST['first_name']) == None):
                context = {}
                context['errorfname'] = 'This First Name Is Not Valid Enter Valid Name'
                return render(request, 'editprofile.html', context)
            if (re.search(name_regex, request.POST['last_name']) == None):
                context = {}
                context['errorlname'] = 'This Last Name Is Not Valid Enter Valid Name'
                return render(request, 'editprofile.html', context)
            if (re.search(phone_regex, request.POST['phone_number']) == None):
                context = {}
                context[
                    'errorphone'] = 'Phone number must be entered in the format: "01[0125][0-9]{8}". Exactly 11 digits allowed.'
                return render(request, 'editprofile.html', context)
            edituser = Usercrowd.objects.filter(id=int(request.POST['id'])).update(
                first_name=request.POST['first_name'], last_name=request.POST['last_name'],
                phone_number=request.POST['phone_number'],
                birthdate=request.POST['birthdate'],
                country=request.POST['country'], facebooklink=request.POST['facebooklink']
            )
            return render(request, 'successregister.html')
        else:
            user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
            if user:
                return render(request, 'editprofile.html', {'user': user})
    else:
        return redirect('login')


def deleteprofile(request):
    if request.session.has_key('user_name'):
        if request.method == 'POST':
            user = Usercrowd.objects.filter(id=int(request.session['user_id']))[0]
            if user:
                user.delete()
                return redirect('logout')

    else:
        return redirect('login')

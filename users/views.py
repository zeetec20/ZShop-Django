from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from zshop.Email import Email
from zshop.settings import ALLOWED_HOSTS

class Auth(View):
    mode = ''

    def get(self, request):
        if (self.mode != ''): raise Http404
        context = {
        
        }
        if (request.user.is_authenticated):
            self.template_name = 'user/index.html'
            return render(request, self.template_name, context)
        else:
            self.template_name = 'user/auth.html'
            context['mode'] = ''
            if ("mode" in request.GET): context['mode'] = request.GET['mode']
            return render(request, self.template_name, context)

    def login(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if (user != None): 
            login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Success Log In', extra_tags='login')
            return redirect('store:index')
        else:
            target_redirect = reverse('user:auth')
            messages.add_message(request, messages.ERROR, 'Failed Log In', extra_tags='login')
            return redirect('{}{}'.format(target_redirect, '?mode=login'))

    def register(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.saveUserClient()
            target_redirect = reverse('user:auth')
            messages.add_message(request, messages.SUCCESS, 'Success Register', extra_tags='register')
            email_user = form.cleaned_data.get('email')
            User = get_user_model()
            user = User.objects.filter(username=form.cleaned_data.get('username'))
            message_email = 'http://{}:8000/user/verification/{}/{}'.format(ALLOWED_HOSTS[0], user[0].username, user[0].verification_code)
            email = Email(subject='Click link to verification your account', message=message_email, email='jusles363@gmail.com', target_list=[email_user])
            email.send()
            return redirect('{}{}'.format(target_redirect, '?mode=register'))
        else:
            target_redirect = reverse('user:auth')
            messages.add_message(request, messages.ERROR, 'Failed Register', extra_tags='register')
            return redirect('{}{}'.format(target_redirect, '?mode=register'))

    def logout(self, request):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'Success Log Out', extra_tags='logout')
        return redirect('store:index')

    def post(self, request):
        if (self.mode == 'login'):
            return self.login(request)
        if (self.mode == 'register'):
            return self.register(request)
        if (self.mode == 'logout'):
            return self.logout(request)

class User_Verification(View):
    def get(self, request, username='', code=''):
        if (request.user.is_authenticated): raise Http404
        User = get_user_model()
        user = User.objects.filter(username=username, verification_code=code)
        if (len(user) == 0):
            messages.add_message(request, messages.ERROR, 'Failed verivication {}'.format(user.username), extra_tags='user_verification')
            return redirect('store:index')
        else:
            user = user[0]
            user.is_active = True;
            user.save()
            messages.add_message(request, messages.SUCCESS, 'Success verivication {}'.format(user.username), extra_tags='user_verification')
            return redirect('store:index')
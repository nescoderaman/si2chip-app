from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import password_reset
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.contrib.auth import logout
# Create your views here.
from django.contrib import messages
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from login.forms import RegistrationForm


def logout_page(request):
    logout(request)
    messages.info(request, 'You have successfully logged out. Come back soon.')
    return HttpResponseRedirect('/')

@login_required
def dashbord(request):
    return password_reset(request, template_name='user/dashbord.html',
        post_reset_redirect=reverse('success'))
@login_required
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']

            )
            return HttpResponseRedirect('/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })

    return render_to_response(
    'registration/register.html',
    variables,
    )
@login_required
def register_success(request):
    return password_reset(request, template_name='registration/success.html',
        post_reset_redirect=reverse('success'))

def resetpage(request):
    return password_reset(request, template_name='forgetpass.html',
        email_template_name='password_reset_email.html',
        post_reset_redirect=reverse('success'))

from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('password_reset_completed'))


def password_reset_completed(request):
    return password_reset(request, template_name='password_reset_complete.html',
        post_reset_redirect=reverse('success'))

def reset(request):
    return password_reset(request, template_name='forgetpass.html',
        email_template_name='password_reset_email.html',
        post_reset_redirect=reverse('success_pass'))
def success(request):
    return password_reset(request, template_name='update_success.html',
        post_reset_redirect=reverse('success'))
def password_reset_complete(request):
    return HttpResponseRedirect('/completed',)

def profile(request):
    return password_reset(request, template_name='user/profile.html',
        post_reset_redirect=reverse('success'))

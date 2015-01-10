from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.db import IntegrityError

from login.models import UserDetails

import logging

# Getting logger instance
login_logger = logging.getLogger(__name__)

#
# Login logic
#
def index(request):
	if request.user.is_authenticated():
		return redirect(reverse('home:index'), permenant=True)
	else:
		return render(request, 'login/index.html')

def auth(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			return redirect(reverse('home:index'), permenant=True)
		else:
			return render(request, 'login/index.html',{
					'error_message': 'Disabled account. Contact Administrator',
				})
	else:
		return render(request, 'login/index.html', {
				'error_message': 'Invalid Username or password',
			})

def outlog(request):
	logout(request)
	return redirect(reverse('login:index'), permenant=True)

#
# Registration logic
#
def register(request):
	context = {}
	if request.POST.get('submit') is not None:
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirm = request.POST['confirm']
		try:
			if password == confirm:
				ud = UserDetails.objects.create_user_details(username,email,password)
				context = {
					"success_message":"Successfully Registered",
					}
			else:
				context = {
					"error_message":"Password mismatch",
					}
		except IntegrityError:
			login_logger.error("username exist")
			context = {
				"error_message":"Username already exist",
				}

	return render(request, 'login/register.html', context)



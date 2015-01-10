from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate

import logging

# Getting logger instance
login_logger = logging.getLogger(__name__)

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

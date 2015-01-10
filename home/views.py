from django.shortcuts import render
from django.http import HttpResponse

import logging

# Getting logger instance
home_logger = logging.getLogger(__name__)


def index(request):
	return render(request, 'home/index.html')

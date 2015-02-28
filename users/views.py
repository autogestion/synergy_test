from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse


def index(request):
    return render(request, 'base.html')

class HomeView(RedirectView):
	"""Redirects to users list view.
	"""
	
	@property
	def url(self):
	    return reverse('users')

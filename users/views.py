from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.views.generic.base import TemplateView

from .models import SynergyUser


class HomeView(RedirectView):
	"""Redirects to users list view.
	"""	
	@property
	def url(self):
	    return reverse('users')

class UserListView(TemplateView):
    template_name = 'users/users_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        
        context['users_count'] = SynergyUser.objects.count()
        #import pdb; pdb.set_trace()
        
        name_patt = self.request.GET.get('searchName')
        if name_patt is None:
            context['users'] = SynergyUser.objects.raw('SELECT * FROM users_synergyuser')
        else:
            context['users'] = SynergyUser.objects.raw('SELECT * FROM users_synergyuser, auth_user WHERE users_synergyuser.user_ptr_id = auth_user.id AND auth_user.username LIKE \'{0}%%\' '.format(name_patt))
        return context

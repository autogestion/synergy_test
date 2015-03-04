from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse
from django.views.generic.base import View
from django.views.generic.base import TemplateView
from django.db import connection
from django.contrib.auth.models import User

from .models import SynergyUser
from .forms import SynergyUserForm


class HomeView(RedirectView):
	"""Redirects to users list view.
	"""	
	@property
	def url(self):
	    return reverse('users')

class UserListView(TemplateView):
    """
    """
    template_name = 'users/users_list.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        #import pdb; pdb.set_trace()
        
        name_patt = self.request.GET.get('searchName')
        context["form"] = SynergyUserForm()

        if name_patt is None:
            context['users'] = SynergyUser.objects.raw('SELECT * FROM users_synergyuser')
        else:
            context['users'] = SynergyUser.objects.raw('SELECT * FROM users_synergyuser, auth_user WHERE users_synergyuser.user_ptr_id = auth_user.id AND auth_user.username LIKE \'{0}%%\' '.format(name_patt))
        return context

class UserOperationView(View):
    """
    """
    form_class = SynergyUserForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            user_id = request.POST.get('user_id')
            if user_id:
                cursor.execute('UPDATE auth_user SET username=\'{}\', email=\'{}\' WHERE id={}'.format(form.cleaned_data['username'], form.cleaned_data['email'], user_id))
                cursor.execute('UPDATE users_synergyuser SET phone={} WHERE user_ptr_id={}'.format(form.cleaned_data['phone'], user_id))
            else:
                user = User.objects.create_user(form.cleaned_data["username"], email=form.cleaned_data['email'])
                cursor.execute('INSERT INTO users_synergyuser (user_ptr_id, phone) VALUES ({}, {})'.format(user.id, form.cleaned_data['phone']) )
            
            return HttpResponseRedirect('/')

        return HttpResponse('ERROR', status=305)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

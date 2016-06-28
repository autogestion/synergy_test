from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.db import connection
from django.contrib.auth.models import User
from django.shortcuts import render

from users.models import SynergyUser, SynergyUserForm


class UserView(View):

    def get(self, request, *args, **kwargs):
        context = {'form': SynergyUserForm()}

        name_patt = request.GET.get('searchName')
        if name_patt is None:
            context['users'] = SynergyUser.objects.raw('SELECT * FROM users_synergyuser')
        else:
            context['users'] = SynergyUser.objects.raw('SELECT * FROM users_synergyuser, auth_user WHERE users_synergyuser.user_ptr_id = auth_user.id AND auth_user.username LIKE \'{0}%%\' '.format(name_patt))

        return render(request, 'users_list.html', context)

    def post(self, request, *args, **kwargs):
        form = SynergyUserForm(request.POST)
        if form.is_valid():
            cursor = connection.cursor()
            user_id = request.POST.get('user_id')
            if user_id:
                cursor.execute('UPDATE auth_user SET username=\'{}\', email=\'{}\' WHERE id={}'.format(
                    form.cleaned_data['username'], form.cleaned_data['email'], user_id))
                cursor.execute('UPDATE users_synergyuser SET phone={} WHERE user_ptr_id={}'.format(
                    form.cleaned_data['phone'], user_id))
            else:
                user = User.objects.create_user(form.cleaned_data["username"], email=form.cleaned_data['email'])
                cursor.execute('INSERT INTO users_synergyuser (user_ptr_id, phone, mobile, status) VALUES ({}, {}, {}, {})'.format(
                    user.id, form.cleaned_data['phone'], form.cleaned_data['mobile'], form.cleaned_data['status']))

            return HttpResponseRedirect('/')

        return HttpResponse('ERROR', status=305)

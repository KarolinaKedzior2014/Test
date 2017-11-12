from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . import manager
import json

# Create your views here.


def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        try:
            user = manager.create_user(data)
        except manager.MissingValuesException as mve:
            msg = 'Missing values: {}'.format(mve)
            return HttpResponse(msg, status=400)
        return HttpResponse('User {} created'.format(user))
    else:
        return HttpResponse('Not found', status=404)


def log_in(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data['login'] if 'login' in data else None
        password = data['password'] if 'password' in data else None
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/app')
        else:
            return HttpResponse('Invalid login or password', status=401)
    else:
        return HttpResponse('Not found', status=404)
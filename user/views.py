from django.db import connection
from django.shortcuts import render
from .forms import LoginForm, RegisterForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            cursor = connection.cursor()
            query = ''' SELECT id 
                        FROM user   
                        WHERE username = '{username}' AND password = '{password}' '''.format(
                username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            cursor.execute(query)
            user = cursor.fetchone()
            if user:
                context['is_logged_in'] = True
                context['username'] = form.cleaned_data['username']
            else:
                context['error'] = 'username or password is wrong.'
    else:
        form = LoginForm()
        context = {'form': form}
    return render(request, 'user/login.html', context)

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            context['is_registered'] = True
            context['username'] = form.cleaned_data['username']
    else:
        form = RegisterForm()
        context = {'form': form}
    return render(request, 'user/register.html', context)

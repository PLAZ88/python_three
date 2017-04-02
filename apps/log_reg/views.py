from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
from ..quote.models import Quote, Favorite
from django.db.models import Count


def index(request):
    return redirect('/main')

def main(request):
    return render(request, 'log_reg/index.html')

def login(request):

    result = User.objects.login(request.POST.copy())
    if 'errors' in result:
        for error in result['errors']:
            messages.add_message(request, messages.ERROR, error)

        return redirect('/')
    request.session['user'] = result['user'].first_name
    request.session['action'] = 'login'
    request.session['user_id'] = result['user'].id

    return redirect('/dashboard')

def register(request):

    result = User.objects.register(request.POST.copy())

    if 'errors' in result:
        for error in result['errors']:
            messages.add_message(request, messages.ERROR, error)

        return redirect('/')
    request.session['user'] = result['user'].first_name
    request.session['action'] = 'register'
    request.session['user_id'] = result['user'].id

    return redirect('/dashboard')

def logout(request):

    request.session.clear()
    return redirect('/')

def dashboard(request):

    if 'user_id' not in request.session:
        return redirect('/main')

    x = Favorite.objects.filter(users_id=request.session['user_id'])

    context = {
        "all_quotes": Quote.objects.exclude(quote_favorite=x),
        # "all_quotes": Quote.objects.all(),
        "favorites": Favorite.objects.filter(users_id=request.session['user_id']),
    }

    return render(request, 'log_reg/dashboard.html', context)



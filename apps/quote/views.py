from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from ..log_reg.models import User
from .models import Quote, Favorite
from django.db.models import Count


def process(request):

    if len(request.POST['author']) < 3:
        messages.add_message(request, messages.WARNING, "Quote authors must be greater than 3 characters")
        return redirect('/dashboard')
    if len(request.POST['quote']) < 10:
        messages.add_message(request, messages.WARNING, "Messages must be more than 10 characters")
        return redirect('/dashboard')

    x = User.objects.get(id=request.session['user_id'])
    Quote.objects.create(quote=request.POST['quote'], author=request.POST['author'], creator = x)


    return redirect('/dashboard')

def feature(request, id):

    if 'user_id' not in request.session:
        return redirect('/main')

    context = {

        "quotes": Quote.objects.filter(creator__id=id),
        "users": User.objects.filter(id=id),
        "totals": User.objects.annotate(num_quotes=Count('quotes')).filter(id=id)
    }

    return render(request, 'quote/feature.html', context)


def remove(request, id):

    Favorite.objects.get(id=id).delete()

    return redirect ('/dashboard')

def repeatprocess(request, id):

    y = User.objects.get(id=request.session['user_id'])
    x = Quote.objects.get(id = id)
    Favorite.objects.create(quote = x , users = y)

    return redirect('/dashboard')


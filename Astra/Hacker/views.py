from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from Hacker.models import Contact
from django.contrib import messages



def index(request):
    messages.success (request,"Welcome to the website of Himalayan Warriors")
    return render (request, 'index.html')


def sponsors (request):
    return render (request, 'sponsors.html' )
   

def contact(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact (name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!.')
    return render (request,'contact.html' )
   

def membership(request):
    return render (request,'membership.html' )

def order(request):
    return render (request, 'order.html')

def players(request):
    return render (request, 'players.html')

def programs(request):
    return render (request,'programs.html' )

def search(request):
    return render (request, 'search.html')

def tracker(request):
    return render (request, 'tracker.html')

def checkout(request):
    return render (request, 'checkout.html')
import random
from django.http import request
from django.shortcuts import render
#from django.http import HttpResponse
from random import choice

# Create your views here.

def home(req):
    return render(req,'generator/home.html')

def about(req):
    return render(req,'generator/about.html')

def password(req):
    #Crea una lista de elementos para devolver
    chars = list('abcdefghijklmnopqrstuvwxyz')
    generated_pass = ''
    length = int(req.GET.get('length'))

    if req.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if req.GET.get('special'):
        chars.extend(list('!@#$%^&*()'))
    
    if req.GET.get('numbers'):
        chars.extend(list('0123456789'))

    for x in range(length):
        generated_pass += choice(chars)
    
    return render(req,'generator/password.html',{'password':generated_pass})
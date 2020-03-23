from django.shortcuts import render
import random

# Create your views here.
def home(request):
    return render(request , 'pass_generator/home.html' , {'variable':"soy_variable"} )

def password(request):   

    characthers = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characthers.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('s_character'):
        characthers.extend(list('!@#$%^&*()`~'))

    if request.GET.get('numbers'):
        characthers.extend(list('1234567890'))
    
    
    lenght = int(request.GET.get('lenght',12))
    thepassword = ''
    for x in range(lenght): 
        thepassword += random.choice(characthers)

    
    return render(request , 'pass_generator/password.html',{'password':thepassword})

def about(request):
    return render(request , 'pass_generator/about.html' )
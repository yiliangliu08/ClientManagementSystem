from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *


def home(request):
    context = {
        "page_title" : "GDog CMS"
    }
    return render(request, 'cms/home.html',context)

def about(request):
    return render(request, 'cms/about.html')
    

def create_client(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        print(name+">"+phone+">"+email)

        cclient = Client(name=name, phone=phone, email=email)
        cclient.save()  

    return render(request, 'cms/create_client.html')


@csrf_exempt
def create_client_test(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.POST)
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        print(name+">"+phone+">"+email)
        cclient = Client(name=name, phone=phone, email=email)
        cclient.save()
    return HttpResponse(status=200)

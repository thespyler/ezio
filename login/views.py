from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse


def hello(request):
    return render(request, 'main.html')

def blog1(request):
    return render(request, 'blog1.html')
# Create your views here.

def blog2(request):
    return render(request, 'blog2.html')

def blog3(request):
    return render(request, 'blog3.html')
def next(request):
    name = request.POST['user']
    # password = request.POST['pass']
    # if password == 'thespyler':
    #     # HttpResponse('Hello' + name)
    HttpResponseRedirect('/ezio/', {'name': name})
    # else:
    #     HttpResponse('wrong password!')

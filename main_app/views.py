from time import monotonic_ns
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def moto_index(request):
    return render(request, 'moto/index.html', {'moto': moto})
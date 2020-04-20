from django.shortcuts import render
from .forms import GeeksModelForm
# Create your views here.

def home_view(request):
    context = {}
    context['form'] = GeeksModelForm()
    return render(request,'djangoform/home.html',context)
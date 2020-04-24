from django.http import request
from django.shortcuts import render
from .forms import InputForm

# Create your views here.
def home_view(reuest):
    context = {}
    context['form'] = InputForm()
    return render(request,"home.html",context)

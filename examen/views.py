from django.shortcuts import render
from django.db.models import Q,Prefetch
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from .forms import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def mi_error_400(request,exception=None):
    return render(request,"errors/400.html",None,None,400)

def mi_error_403(request,exception=None):
    return render(request,"errors/403.html",None,None,403)

def mi_error_404(request,exception=None):
    return render(request,"errors/404.html",None,None,404)

def mi_error_500(request,exception=None):
    return render(request,"errors/500.html",None,None,500)
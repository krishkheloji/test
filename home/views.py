from demoproject.home.forms import ContactForm
from django.shortcuts import render
from home.forms import EmpForm
# Create your views here.

def index(request):  
    
    return render(request,"index.html") 
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def vista1_app2(request):
    return render(request, 'app2/v1.html')

def vista2_app2(request):
    return render(request, 'app2/v2.html')
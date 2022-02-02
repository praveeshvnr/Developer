from django.http import request
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')
def applyleave(request):
    return render(request,'applyleav.html')
def applyleav1(request):
    return render(request,'applyleav1.html')
def applyleav2(request):
    return render(request,'applyleav2.html')
def leaverequiest(request):
    return render(request,'leaverequiest.html')
def drattendance(request):
    return render(request,'drattendance.html')





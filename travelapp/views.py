from django.http import HttpResponse
from django.shortcuts import render
from .models import place

# Create your views here

def demo(request):
    obj=place.objects.all()
    # print(obj[0])
    return render (request,"index.html",{'result':obj} )









# def demo(request):
#      return HttpResponse("hello world")
    
# def about(request):
#      name="nothing"
#      return render(request,"about.html",{'obj':name})
# def contact(request):
#     return HttpResponse("contacting to")
# # def demo(request):
# #     Name="India"
# #     return render (request,"home.html",{'obj':Name})
# def addition(request):
#     x=int(request.GET['number1'])
#     y=int(request.GET['number2'])
#     res=x+y
#     return render(request,"result.html",{'result':res})
# def demo(request):
#     return render(request,"hi.html")
# def work(request):
#     return render(request,"trial.html")
def login(request):
    return HttpResponse("login here")

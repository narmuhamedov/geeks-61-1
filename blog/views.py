from django.shortcuts import render
from django.http import HttpResponse

#функция вывода hello world
def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse("Hello World")
    
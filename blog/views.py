from django.shortcuts import render
from django.http import HttpResponse

#функция вывода hello world
def hello_world_view(request):
    if request.method == "GET":
        return HttpResponse("Hello World")
    

def name(request):
    if request.method == 'GET':
        return HttpResponse('<strong>Radomir Backend Dev</strong>')


def photo(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTisBhbjzS_pcpcNSl2TJXmgi0jUeME-bYhIA&s">')
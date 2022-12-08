from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def show_main_page(request):
    return HttpResponse('{"status": "ok"}')

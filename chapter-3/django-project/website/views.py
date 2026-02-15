from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse,JsonResponse

def home_view(request):
    return HttpResponse("home")


def about_view(request):
    return HttpResponse("about")

def contact_view(request):
    return HttpResponse("contact")
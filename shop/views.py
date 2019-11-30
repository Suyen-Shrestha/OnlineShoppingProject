from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "shop/index.html")


def about_view(request):
    return HttpResponse("This is from about view")


def contact_view(request):
    return HttpResponse("This is from about view")


def tracker_view(request):
    return HttpResponse("This is from about view")


def search_view(request):
    return HttpResponse("This is from about view")


def product_view(request):
    return HttpResponse("This is from about view")


def checkout_view(request):
    return HttpResponse("This is from about view")

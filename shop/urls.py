from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('about/', views.about_view, name="about"),
    path('contact/', views.contact_view, name="contact"),
    path('tracker/', views.tracker_view, name="tracker"),
    path('search/', views.search_view, name="search"),
    path('productview/', views.product_view, name="productview"),
    path('checkout/', views.checkout_view, name="checkout"),



]

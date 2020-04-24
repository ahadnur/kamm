from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about_us, name="about-us"),
    path('programs/', views.programs, name="programs"),
    path('contact/', views.contact, name="contact"),
    path('charitable-autist/', views.ch_autist, name="ch-autist"),
]

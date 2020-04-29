from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about_us(request):
    return render(request, 'pages/about.html')

def programs(request):
    return render(request, 'pages/programs.html')

def contact(request):
    return render(request, 'pages/contact.html')


def ch_autist(request):
    return render(request, 'pages/ch_autist.html')


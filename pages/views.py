from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    posts = Post.objects.order_by('date_posted')
    context = {
        'posts': posts
    }
    return render(request, 'pages/home.html', context)

def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'pages/post.html', context)

def about_us(request):
    return render(request, 'pages/about.html')

def programs(request):
    return render(request, 'pages/programs.html')

def contact(request):
    return render(request, 'pages/contact.html')


def ch_autist(request):
    return render(request, 'pages/ch_autist.html')

def running_programs(request):
    return render(request, 'pages/running_programs.html')


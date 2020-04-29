from django.shortcuts import render

def sanitation(request):
    return render(request, 'programs/sanitation.html')

def health(request):
    return render(request, 'programs/health.html')

def awarness(request):
    return render(request, 'programs/awarness.html')

def handicraft(request):
    return render(request, 'programs/handicraft.html')

def education(request):
    return render(request, 'programs/education.html')
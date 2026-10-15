from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def projects(request):
    return render(request, 'projects.html')


def resume(request):
    return render(request, 'resume.html')

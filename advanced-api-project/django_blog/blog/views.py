from django.shortcuts import render


def index(request):
    return render(request, 'your_app/index.html')

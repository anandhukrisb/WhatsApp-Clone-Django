from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

from django.shortcuts import render

def room(request):
    return render(request, 'room.html')

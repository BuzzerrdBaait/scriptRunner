from django.shortcuts import render


def home(request):

    greeting="Welcome to the Home Page!"

    return render(request,'home.html')
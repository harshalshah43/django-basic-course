from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Home Page</h1>")

def about(request):
    return HttpResponse("<h1>This About Us Page</h1>")

from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request,'blog/home.html')
    # return HttpResponse("<h1>Welcome to Home Page</h1>")

def about(request):
    return render(request,'blog/about.html')
    # return HttpResponse("<h1>This About Us Page</h1>")

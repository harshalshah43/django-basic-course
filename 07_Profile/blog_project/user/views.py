from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog-home')

    else:
        form = UserRegistrationForm() # empty form
    return render(request,'user/register.html',{'form':form})


def profile(request):
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST,instance = request.user)
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = UserRegistrationForm(instance = request.user)
    
    return render(request,'user/profile.html',{'u_form':u_form})
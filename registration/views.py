from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home.html')

@login_required
def dashboard(request):
    return render(request,'dashboard.html')
def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form=UserCreationForm()
    return render(request,'registration/register.html',{'form':form})
# def login(request):
#     return render(request,'logout.html')
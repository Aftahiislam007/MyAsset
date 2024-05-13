from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, LoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
        form.save()
        return redirect('user-login')
    else:
      form = CreateUserForm()
      
    context = {
        'form': form, 
    }
    return render(request, 'user/register.html', context) 
  
# login page
# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(request, username=username, password=password)
#             if user:
#                 login(request, user)    
#                 return redirect('dashboard-index')
#     else:
#         form = LoginForm()
        
#     context = {
#         'form': form, 
#     }
#     return render(request, 'user/login.html', context)


def profile(request):
    return render(request, 'user/profile.html')    
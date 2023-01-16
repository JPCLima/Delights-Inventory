from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

from .forms import SignInForm


def login_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('login')

    else:
        form = SignInForm()
        return render(request, 'users/login.html', {'form': form})
""" 
def login_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = SignInForm()        
    return render(request, 'users/login.html', {'form': form})
 """

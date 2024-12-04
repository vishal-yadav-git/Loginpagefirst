from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from .forms import SignUpForm
from django.contrib import messages

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:  # If authentication is successful
            auth_login(request, user)  # Log the user in
            return redirect('welcome')  # Redirect to welcome page after successful login
        else:
            messages.error(request, 'Invalid username or password')  # If authentication fails
            return redirect('signup')  # Redirect to signup page if login fails

    return render(request, 'login.html')  # Return to login form if the method is GET or failed login

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)  # Include request.FILES to handle file uploads
        if form.is_valid():
            form.save()  # Now the profile picture will be saved automatically with the user
            return redirect('login')  # Redirect to the login page or home page after successful signup
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logging out

def welcome(request):
    return render(request, 'welcome.html')  # This should work fine


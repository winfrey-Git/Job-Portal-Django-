from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from jobwebsite.models import UserProfile  # Make sure this import is here

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Access the role from the UserProfile model
            try:
                profile = UserProfile.objects.get(user=user)
                if profile.role == 'employer':
                    return redirect('employer_dashboard')  # Assuming you have this view
                elif profile.role == 'employee':
                    return redirect('employee_dashboard')  # Assuming you have this view
            except UserProfile.DoesNotExist:
                messages.error(request, "User profile not found")
                return redirect('login')
        
        else:
            messages.error(request, "Invalid username or password")
            return redirect('login')

    return render(request, 'login.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from jobwebsite.models import UserProfile  
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator

def register_view(request):
    if request.method == 'POST':
        # Corrected POST attribute name
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        role = request.POST['role']  # Assuming 'role' is a field in your form

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        
        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        try:
            RegexValidator(r'^[\w]{3,30}$', 'Username must be 3-30 characters long and can only contain letters, numbers, and underscores.')(username)

        except ValidationError as e:
            messages.error(request, "Invalid username: " + str(e) )
            return redirect('register')
        
        try:
            EmailValidator()(email)
        except ValidationError:
            messages.error(request, "Invalid email format")
            return redirect('register') 
        
        try:
            validate_password(password1)
        except ValidationError as e:
            for error in e:
                messages.error(request, error)
            return redirect('register') 
                   
        # Create user and UserProfile
        user = User.objects.create_user(username=username, password=password1, email=email)  # Fixed argument name
        UserProfile.objects.create(user=user, role=role)  # Create UserProfile for the user
        user.save()

        messages.success(request, "Registration successful, please log in.")
        return redirect('login')

    return render(request, 'register.html')  # Ensure 'register.html' exists in your templates directory

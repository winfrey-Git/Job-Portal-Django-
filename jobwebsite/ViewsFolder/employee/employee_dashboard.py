from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobwebsite.models import UserProfile

@login_required
def employee_dashboard_view(request):
    if request.user.userprofile.role == 'employee':
        return render(request, 'job_seeker/employee_dashboard.html')
    
    else:
        messages.error(request, 'Access denied.This page is for employees only.')
        return redirect('home')
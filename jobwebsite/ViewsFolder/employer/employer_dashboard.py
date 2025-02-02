from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from jobwebsite.models import Job

@login_required
def employer_dashboard_view(request):
    jobs = Job.objects.filter(user=request.user)  # Assuming a user relation
    context = {
        'jobs': jobs,
        'total_jobs': jobs.count(),
        'active_applications': jobs.filter(status='open').count(),
        'pending_reviews': jobs.filter(status='pending').count()
    }
    return render(request, 'employer_dashboard.html', context)

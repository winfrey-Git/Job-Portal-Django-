from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from jobwebsite.models import Applicant
from jobwebsite.forms import ApplyJobForm
from django.contrib import messages

from jobwebsite.permissions import user_is_employee

#@login_required(login_url=reverse_lazy('jobwebsite:login'))
@user_is_employee
def apply_job_view(request, id):
    user = request.user
    if Applicant.objects.filter(user=user, job=id).exists():
        messages.error(request, 'You already applied for this job!')
    else:
        if request.method == 'POST':
            form = ApplyJobForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = user
                instance.save()
                messages.success(request, 'You have successfully applied for this job!')
        else:
            messages.error(request, 'Invalid request.')
    return redirect(reverse("jobwebsite:single-job", kwargs={'id': id}))
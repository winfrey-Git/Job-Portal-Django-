from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib import messages
from jobwebsite.models import Category
from jobwebsite.forms import JobForm

@login_required(login_url=reverse_lazy('login'))
def create_job_view(request):
    # Ensure the user is an employer
    if request.user.role != 'employer':
        messages.error(request, "You do not have permission to create a job post.")
        return redirect('home')

    form = JobForm(request.POST or None)
    categories = Category.objects.all()

    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user  # Associate the job with the logged-in employer
        instance.save()
        form.save_m2m()  # Save tags for many-to-many fields
        messages.success(request, 'You have successfully posted your job! Please wait for review.')
        return redirect(reverse("single_job", kwargs={'id': instance.id}))

    context = {
        'form': form,
        'categories': categories,
    }
    return render(request, 'post_job.html', context)

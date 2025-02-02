from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, Group, Permission
from taggit.managers import TaggableManager
from django.contrib.auth import get_user_model
from jobwebsite.managers import CustomUserManager

from ckeditor_uploader.fields import RichTextUploadingField




User = get_user_model()

# Choices for job types,role and gender
JOB_TYPE = (( "full time", "Full time"), ( "part time", "Part time"), ("internship", "Internship"))
GENDER_TYPE = (("M", "Male"), ("F", "Female"))
ROLE_CHOICES = (('employer', 'Employer'),('employee', 'Employee'))


class Category(models.Model):
    name = models.CharField(max_length=225)

    def __str__(self):
        return self.name

class Job(models.Model):
    user = models.ForeignKey(User, related_name="posted_jobs", on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    company_name = models.CharField(max_length=225)
    company_description = models.TextField()  # Changed to TextField for longer descriptions
    description = models.TextField()  # Changed to TextField for more detailed job descriptions
    location = models.CharField(max_length=225)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    category = models.ForeignKey(Category, related_name="jobs", on_delete=models.CASCADE)
    salary = models.CharField(max_length=100, blank=True)
    posted_date = models.DateTimeField(auto_now_add=True)
    deadline_date = models.DateTimeField()
    is_published = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)  # Added to mark featured jobs
    timestamp = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    #url = models.URLField(max_length=200)
    tags = TaggableManager()

    def __str__(self):
        return f"{self.title} at {self.company_name}"

    def get_absolute_url(self):
        return reverse('job_detail', args=[str(self.id)])

class Applicant(models.Model):
    user = models.ForeignKey(User, related_name="applicant_profiles", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name="applicants", on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)  # Changed to CharField for better phone formatting
    gender = models.CharField(choices=GENDER_TYPE, max_length=10)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} applied for {self.job.title}"

class Favorite(models.Model):
    user = models.ForeignKey(User, related_name="favorited_jobs", on_delete=models.CASCADE)
    job = models.ForeignKey(Job, related_name="favorites", on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    soft_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} favorited {self.job.title}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"
    

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, blank=False, error_messages={'unique': "A user with that email already exist."})

    role = models.CharField(choices=ROLE_CHOICES,max_length=10)
    gender = models.CharField(choices=GENDER_TYPE, max_length=1)

        # Custom related_name attributes to avoid clashes
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Custom related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Custom related_name
        blank=True
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.first_name+ ' ' +self.last_name
    objects = CustomUserManager()
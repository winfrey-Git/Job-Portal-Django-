from django import forms
from jobwebsite.models import Applicant
from jobwebsite.models import User
from django.contrib.auth.forms import UserCreationForm
class ApplyJob(forms.ModelForm):
    class meta:
        model=User
        field = ['first_name', 'last_name','email', 'password1','password2']

        labels = {
            'first_name': 'Company Name:',
            'last_name': 'Company Address:',
            'email': 'Email Address:',
            'password1': 'Password:',
            'password2': 'Confirm Password:',
        }

        widgets= {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter Company Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Company Address'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'password1': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
            'password2': forms.PasswordInput(attrs={'placeholder': 'Enter Password'}),
        }


def save(self, commit=True):
    user = UserCreationForm.save(self, commit=False)
    user.role = "employer"
    if commit:
        user.save()
    return user
from django import forms
from jobwebsite.models import User

class EmployeeProfileEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "gender"]
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'Enter First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Enter Last Name'}),
        }

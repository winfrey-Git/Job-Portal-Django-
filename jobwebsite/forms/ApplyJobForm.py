from django import forms
from jobwebsite.models import Applicant
from ckeditor.widgets import CKEditorWidget

class JobApplyForm(forms.ModelForm):
    class meta:
        model = Applicant
        fields = ['job'] 
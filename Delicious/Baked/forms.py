from django import forms
from .models import registeration
from .models import Contact
# Create your models here.

class registerform(forms.ModelForm):
    class Meta:
        model = registeration
        fields = ['Name', 'Email', 'Password', 'Confirmpass']

class loginform(forms.ModelForm):
    class Meta:
        model = registeration
        fields = ['Email', 'Password']

class Contactform(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['Name', 'Email', 'Subject', 'Message', 'File']
from django import forms
from django.forms import ModelForm
from .models import *


class TaskForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task Title...'}), label=False)
    due=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Due Date...'}), label=False)
    class Meta:
        model =task
        fields=['title','due']


class UpgateForm(forms.ModelForm):
    title = forms.CharField(widget= forms.TextInput(attrs={'placeholder':'Task Title...'}), label=False)

    class Meta:
         model=task
         fields=['title','due','complete']


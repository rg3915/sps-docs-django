from django import forms

from .models import SPSElement


class SPSElementForm(forms.ModelForm):

    class Meta:
        model = SPSElement
        fields = '__all__'

"""import form class from django """
from django import forms
# import GeeksModel from models.py
from .models import GeeksModel

class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = '__all__'



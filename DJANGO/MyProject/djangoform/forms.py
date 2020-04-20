from django import forms
from .models import GeeksModel

class GeeksModelForm(forms.ModelForm):
    class Meta:
        model = GeeksModel
        fields = '__all__'
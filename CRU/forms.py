from django import forms
from .models import Measurement

class ValidChol(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = '__all__'
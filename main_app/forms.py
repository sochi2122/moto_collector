from dataclasses import field
from django.forms import ModelForm
from .models import Mile

class MileForm(ModelForm):
    class Meta:
        model = Mile
        fields = ('date',)

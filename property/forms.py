from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['owner', 'place', 'area', 'location', 'bedrooms', 'bathrooms', 'hospitals_nearby', 'colleges_nearby']
from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cat, User


class CatForm(forms.Form):
    class Meta:
        model = Cat
        fields = ['name', 'age', 'breed', 'hair_type']
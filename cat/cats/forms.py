from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cat, User


class CatForm(forms.ModelForm):
    name = forms.CharField()
    age = forms.IntegerField()
    breed = forms.CharField()
    hair_style = forms.ChoiceField(choices=[('long', 'Длинная шерсть'), ('short', 'Короткая шерсть')])
    class Meta:
        model = Cat
        fields = ['name', 'age', 'breed', 'hair_type']

    def save(self, commit=True):
        cat = self.instance
        if commit:
            cat.save()
        return cat

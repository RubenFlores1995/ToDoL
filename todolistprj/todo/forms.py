from django import forms
from .models import todo


class todoForm(forms.Form):
    nombre = forms.CharField()
    url = forms.URLField()


class todoModelForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = '__all__' #nombre
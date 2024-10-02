from django import forms

class ExampleForm(forms.Form):
    author = forms.CharField(max_length=100, required=False)
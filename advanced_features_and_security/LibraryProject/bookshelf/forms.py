from django import forms

class BookSearchForm(forms.Form):
    author = forms.CharField(max_length=100, required=False)
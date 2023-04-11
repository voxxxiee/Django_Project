from logging import PlaceHolder
from django import forms
from django.forms import widgets
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'genre', 'number_of_pages')

        widgets = {
                'title': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
                'author': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
                'genre': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
                'number_of_pages': forms.NumberInput(attrs={'class': 'form-control', 'required': True}),
        }

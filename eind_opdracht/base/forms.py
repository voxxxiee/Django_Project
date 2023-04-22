from logging import PlaceHolder
from django import forms
from django.forms import widgets
from .models import Book, Read, Profile


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


class LeesActieForm(forms.ModelForm):
    class Meta:
        model = Read
        fields = ('book', 'date', 'score')

        widgets = {
            'book': forms.Select(attrs={'class': 'form-select', 'required': True}),
            'date': forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date', 'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'type': 'range', 'min': 0, 'max': 5, 'class': 'form-range', 'required': True}),
        }

    def __init__(self, *args, **kwargs):
        super(LeesActieForm, self).__init__(*args, **kwargs)
        books = Book.objects.filter(approved=True)
        self.fields['book'].queryset = books


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('city', 'date_of_birth' ,'biotext')

        widgets = {
            'city': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
            'date_of_birth': forms.DateInput(format="%Y-%m-%d", attrs={'type': 'date', 'class': 'form-control'}),
            'biotext': forms.Textarea(attrs={'class': 'form-control', 'required': True}),
        }

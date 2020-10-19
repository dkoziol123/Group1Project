from django import forms
from .models import Book, Movie, Magazine


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'genre', 'quantity', 'isbn')


class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ('magazine_name', 'genre', 'quantity')


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('movie_name', 'subject', 'series', 'quantity')
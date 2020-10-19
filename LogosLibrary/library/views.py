from django.shortcuts import render
from .models import *
from .forms import *


def book_list(request):
    book = Book.objects.filter()
    return render(request, 'library/book_list.html',
                 {'books': book})

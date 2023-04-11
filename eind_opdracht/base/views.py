from django.shortcuts import get_object_or_404, redirect, render
from django.utils.formats import numberformat
from .models import Book
from .forms import BookForm
from django.contrib import messages


def index(request):
    return render(request, 'base/index.html')


def add_book(request, pk=None):
    if request.method == "POST":
        print("BOE")
        if pk is not None:
            book = Book.objects.get(pk=pk)
            form = BookForm(request.POST, instance=book)
        else:
            form = BookForm(request.POST)

        # om te checken of het boek niet stiekem al bestaat
        title = request.POST.get("title")
        author = request.POST.get("author")
        # om te checken of het gegeven getal niet -1 is oid
        number_of_pages = int(request.POST.get("number_of_pages"))
        does_exist = Book.objects.filter(title=title, author=author).exists()
        if does_exist is True:
            form.add_error("title", "Dit boek bestaat al van deze schrijver")

        if number_of_pages < 1:
            form.add_error("number_of_pages", "Je moet een positief nummer geven voor het aantal pagina's")

        if form.is_valid():
            form.save()
            messages.success(request, "Het boek is succesvol opgeslagen!")
            return redirect("")
    else:
        if pk is None:
            form = BookForm()
        else:
            book = Book.objects.get(pk=pk)
            form = BookForm(instance=book)
    context = {'form': form}
    return render(request, 'base/add_book.html', context)
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.formats import numberformat
from django.contrib.auth import  login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

from base.forms import LeesActieForm
from .models import Book, Read, Profile
from .forms import BookForm, LeesActieForm, ProfileUpdateForm
from django.contrib import messages


def index(request):
    # pak de laatste 2 leesacties om op de pagina te tonen
    actions = Read.objects.all().order_by('-pk')[:2]
    context = {'actions': actions}
    return render(request, 'base/index.html', context)


@login_required
def add_book(request, pk=None):
    if request.method == "POST":
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
            book = form.save(commit=False)
            if request.user.get_username() == "admin":
                book.approved = True
                book.approved_by = request.user
            book.save()
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


@login_required
def add_read(request, pk=None):
    if request.method == "POST":
        if pk is not None:
            actie = Read.objects.get(pk=pk)
            form = LeesActieForm(request.POST, instance=actie)
        else:
            form = LeesActieForm(request.POST)

        # om te checken of de score niet hoger dan 5 of minder dan 0 is anders werkt een ster rating niet echt
        score = int(request.POST.get("score"))
        if score < 0 or score > 5:
            form.add_error("score", "Je score kan niet minder dan 0 zijn of hoger dan 5")

        # de benodigde input velden om te checken of het boek niet meerdere keren op 1 dag gelezen is.
        date = request.POST.get("date")
        book = request.POST.get("book")
        does_exist = Read.objects.filter(date=date, user=request.user, book=book).exists()
        if does_exist is True and pk is None:
            form.add_error("book", "Je kan niet hetzelfde boek op dezelfde dag lezen")

        if form.is_valid():
            time = form.save(commit=False)
            time.user = request.user
            time.save()
            messages.success(request, "De leesacite is succesvol opgeslagen!")
            # stuur de gebruiker naar zijn/haar pagina met leesacties
            return redirect("base:readfeed", user=request.user)
    else:
        if pk is None:
            form = LeesActieForm()
        else:
            actie = Read.objects.get(pk=pk)
            form = LeesActieForm(instance=actie)

    context = {'form': form}
    return render(request, 'base/add_read.html', context)


def read_feed(request, user=None):
    if user is not None:
        actions = Read.objects.filter(user__username=user)
    else:
        actions = Read.objects.all()
    context = {'actions': actions.order_by('-date')}
    return render(request, 'base/readfeed.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('base:index')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required
def profile_page(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    context = {'profile': profile}
    return render(request, 'base/profile_page.html', context)

@login_required
def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    if request.method == "POST":
        form = ProfileUpdateForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
            return redirect('base:profile')
    else:
        form = ProfileUpdateForm(instance=profile)
    context = {'form': form}
    return render(request, 'base/edit_profile.html', context)
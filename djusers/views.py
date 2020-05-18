from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libra.models import *
from django.contrib.auth.models import User
import mammoth
from jinja2 import Environment, BaseLoader

@login_required
def book_reader(request, id):
    user = request.user

    return render(request, "reader.html", {'user': user, 'book_id': id})

@login_required
def book_about(request, id):
    user = request.user
    if request.user.is_authenticated:
        book_file = book.objects.filter(id = id)[0]

    data = {
        'user': user,
        'book_id': id,
        'description': book_file.description,
        'author': book_file.author,
        'name': book_file.name,
        'release_date': book_file.release_date,
        'category': book_file.category,
        'cover': book_file.cover,
        'file': book_file.book_file,
    }

    return render(request, "book.html", data)


@login_required
def author_about(request, id):
    user = request.user
    if request.user.is_authenticated:
        author_ = author.objects.filter(id = id)[0]
        bookarray = book.objects.filter(author = author_)

    data = {
        'user': user,
        'author_id': id,
        'name': author_.name,
        'description': author_.description,
        'bookarray': bookarray,
    }

    return render(request, "author.html", data)


@login_required
def category_about(request, id):
    user = request.user
    if request.user.is_authenticated:
        category_ = category.objects.filter(id = id)[0]
        bookarray = book.objects.filter(category = category_)

    data = {
        'user': user,
        'author_id': id,
        'name': category_.name,
        'description': category_.description,
        'bookarray': bookarray,
    }

    return render(request, "category.html", data)


@login_required
def category_list(request):
    user = request.user
    if request.user.is_authenticated:
        categoryarray = category.objects.all()

    return render(request, "category_all.html", {'user': user, 'categoryarray': categoryarray})


def home(request):
    user = request.user

    return render(request, "home.html", {'user': user})

def help(request):
    user = request.user

    return render(request, "help.html", {'user': user})

def books(request):
    user = request.user
    bookarray = book.objects.all().order_by('name')

    return render(request, "books.html", {'user': user, 'bookarray': bookarray})


def authors(request):
    user = request.user
    authorarray = author.objects.all().order_by('name')

    return render(request, "authors.html", {'user': user, 'authorarray': authorarray})
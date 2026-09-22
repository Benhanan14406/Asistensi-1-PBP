from datetime import datetime

from django.core import serializers
from django.core.checks import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from main.forms import BookForm
from main.models import Book

# Create your views here.
def home(request):
    return render(
        request,
        'book_list.html'
    )

def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.Info(request, "Buku berhasil ditambahkan.")
            return redirect("main:book_list")
    else:
        form = BookForm()

    context = {"form": form}
    return render(
        request,
        "book_form.html",
        context
    )

# def add_book(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             # Extract validated data and create the model instance manually
#             Book.objects.create(
#                 title=form.cleaned_data["title"],
#                 author=form.cleaned_data["author"],
#                 stock=form.cleaned_data["stock"],
#             )
#             messages.success(request, "Buku berhasil ditambahkan.")
#             return redirect("main:book_list")
#     else:
#         form = BookForm()
#
#     return render(request, "book_form.html", {"form": form})

def get_books_json(request):
    title_query = request.GET.get("title", "").strip()
    books = Book.objects.all()

    if title_query:
        books = books.filter(title__icontains=title_query)

    return HttpResponse(
        serializers.serialize("json", books),
        content_type="application/json",
    )


def get_book_json_by_id(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return HttpResponse(
        serializers.serialize("json", [book]),
        content_type="application/json",
    )

def book_list(request):
    books = Book.objects.all()
    last_visit_cookie = request.COOKIES.get("last_visit", "Belum pernah berkunjung")
    last_visit_session = request.session.get("last_visit_session", "Belum ada session")
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    request.session["last_visit_session"] = current_time

    context = {
        "books": books,
        "last_visit_cookie": last_visit_cookie,
        "last_visit_session": last_visit_session,
    }

    response = render(request, "book_list.html", context)
    response.set_cookie("last_visit", current_time)
    return response
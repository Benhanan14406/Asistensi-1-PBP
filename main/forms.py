from django import forms
from django.core.exceptions import ValidationError
from main.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "stock"]
        labels = {
            "title": "Judul Buku",
            "author": "Penulis",
            "stock": "Jumlah Stok",
        }
        widgets = {
            "title": forms.TextInput(attrs={
                "placeholder": "Masukkan judul buku",
                "maxlength": 150,
            }),
            "author": forms.TextInput(attrs={
                "placeholder": "Masukkan nama penulis",
                "maxlength": 100,
            }),
            "stock": forms.NumberInput(attrs={"min": "0"}),
        }

    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        if stock < 0:
            raise ValidationError("Stok tidak boleh bernilai negatif.")
        return stock
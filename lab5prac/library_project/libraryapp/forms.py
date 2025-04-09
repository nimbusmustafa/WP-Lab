from django import forms
from .models import Book, Borrower, Issue

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowerForm(forms.ModelForm):
    class Meta:
        model = Borrower
        fields = '__all__'

class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['borrower', 'book']

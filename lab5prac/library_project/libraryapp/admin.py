from django.contrib import admin
from .models import Book, Borrower, Issue

admin.site.register(Book)
admin.site.register(Borrower)
admin.site.register(Issue)

# Register your models here.

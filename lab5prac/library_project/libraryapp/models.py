from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=150)
    author=models.CharField(max_length=150)
    isbn=models.CharField(max_length=150)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Borrower(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name
    
class Issue(models.Model):
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
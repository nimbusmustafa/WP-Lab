from django.shortcuts import render, redirect
from .forms import BookForm, BorrowerForm, IssueForm
from .models import Issue

def dashboard(request):
    issues = Issue.objects.all()
    return render(request, 'libraryapp/dashboard.html', {'issues': issues})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BookForm()
    return render(request, 'libraryapp/form.html', {'form': form})

def add_borrower(request):
    if request.method == 'POST':
        form = BorrowerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = BorrowerForm()
    return render(request, 'libraryapp/form.html', {'form': form})

def issue_book(request):
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            issue.book.is_available = False
            issue.book.save()
            return redirect('dashboard')
    else:
        form = IssueForm()
    return render(request, 'libraryapp/form.html', {'form': form})

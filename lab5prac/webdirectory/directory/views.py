from django.shortcuts import render, redirect
from .models import Category, Page
from .forms import CategoryForm, PageForm

def home(request):
    categories = Category.objects.all()
    return render(request, 'directory/home.html', {'categories': categories})

def add_data(request):
    if request.method == 'POST':
        cat_form = CategoryForm(request.POST)
        page_form = PageForm(request.POST)
        if cat_form.is_valid() and page_form.is_valid():
            category = cat_form.save()
            page = page_form.save(commit=False)
            page.category = category
            page.save()
            return redirect('home')
    else:
        cat_form = CategoryForm()
        page_form = PageForm()
    return render(request, 'directory/add_data.html', {'cat_form': cat_form, 'page_form': page_form})

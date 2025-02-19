from django.shortcuts import render

def home(request):
    # Render the home page with the book cover and links
    return render(request, 'book/home.html')

def metadata(request):
    # Render the metadata page
    return render(request, 'book/metadata.html')

def reviews(request):
    # Render the reviews page
    return render(request, 'book/reviews.html')

def publisher(request):
    # Render the publisher info page
    return render(request, 'book/publisher.html')

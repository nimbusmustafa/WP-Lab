# users/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm

# Register page view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Get cleaned data from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            contact_number = form.cleaned_data['contact_number']
            
            # Save the data in the session or process as required
            request.session['username'] = username
            request.session['email'] = email
            request.session['contact_number'] = contact_number

            # Redirect to the success page
            return redirect('success')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

# Success page view
def success(request):
    username = request.session.get('username')
    email = request.session.get('email')
    contact_number = request.session.get('contact_number')

    return render(request, 'success.html', {
        'username': username,
        'email': email,
        'contact_number': contact_number
    })

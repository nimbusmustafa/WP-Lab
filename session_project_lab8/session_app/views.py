from django.shortcuts import render, redirect

# View for the first page (form)
def first_page(request):
    if request.method == 'POST':
        # Store form data in session
        name = request.POST.get('name')
        roll = request.POST.get('roll')
        subject = request.POST.get('subject')
        
        # Store data in session
        request.session['name'] = name
        request.session['roll'] = roll
        request.session['subject'] = subject
        
        # Redirect to second page
        return redirect('second_page')

    # List of subjects for the dropdown
    subjects = ['Math', 'Science', 'History', 'English']
    return render(request, 'session_app/firstPage.html', {'subjects': subjects})

# View for the second page (displaying data from the session)
def second_page(request):
    name = request.session.get('name', 'Not Provided')
    roll = request.session.get('roll', 'Not Provided')
    subject = request.session.get('subject', 'Not Provided')
    
    # Clear session after use (optional)
    # request.session.flush()

    return render(request, 'session_app/secondPage.html', {
        'name': name,
        'roll': roll,
        'subject': subject
    })

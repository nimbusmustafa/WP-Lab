from django.shortcuts import render
from .forms import StudentForm

def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            dob = form.cleaned_data['dob']
            address = form.cleaned_data['address']
            contact_number = form.cleaned_data['contact_number']
            email = form.cleaned_data['email']
            english_marks = form.cleaned_data['english_marks']
            physics_marks = form.cleaned_data['physics_marks']
            chemistry_marks = form.cleaned_data['chemistry_marks']
            
            # Calculate total and percentage
            total_marks = english_marks + physics_marks + chemistry_marks
            total_percentage = (total_marks / 300) * 100
            
            # Return the same form with calculated details
            return render(request, 'student/student_form.html', {
                'form': form,
                'name': name,
                'dob': dob,
                'address': address,
                'contact_number': contact_number,
                'email': email,
                'english_marks': english_marks,
                'physics_marks': physics_marks,
                'chemistry_marks': chemistry_marks,
                'total_percentage': total_percentage
            })
    else:
        form = StudentForm()
    
    return render(request, 'student/student_form.html', {'form': form})

from django.shortcuts import render, redirect

# View for the input page
def input_page(request):
    if request.method == 'POST':
        # Get name and total marks from the form
        name = request.POST.get('name')
        total_marks = request.POST.get('total_marks')

        # Calculate CGPA
        try:
            cgpa = float(total_marks) / 50  # Calculate CGPA
        except ValueError:
            cgpa = 0

        # Store in session
        request.session['name'] = name
        request.session['cgpa'] = cgpa

        return redirect('result')  # Redirect to result page
    
    return render(request, 'calculator/input_page.html')  # Make sure the path is correct

# View for the result page
def result_page(request):
    name = request.session.get('name', 'N/A')
    cgpa = request.session.get('cgpa', 0)
    return render(request, 'calculator/result_page.html', {'name': name, 'cgpa': cgpa})

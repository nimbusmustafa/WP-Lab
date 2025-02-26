from django.shortcuts import render

# List of car manufacturers
CAR_MANUFACTURERS = ['Toyota', 'Ford', 'BMW', 'Tesla', 'Audi']

# View for the form page
def car_form(request):
    if request.method == 'POST':
        manufacturer = request.POST.get('manufacturer')
        model = request.POST.get('model')
        return render(request, 'car_app/result.html', {'manufacturer': manufacturer, 'model': model})

    return render(request, 'car_app/form.html', {'car_manufacturers': CAR_MANUFACTURERS})

# View for displaying the result page
def car_result(request):
    return render(request, 'car_app/result.html')

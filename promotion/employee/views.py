from django.shortcuts import render
from .forms import PromotionEligibilityForm
from datetime import datetime

def check_promotion_eligibility(request):
    if request.method == 'POST':
        form = PromotionEligibilityForm(request.POST)
        if form.is_valid():
            # Get the data from the form
            employee_id = form.cleaned_data['employee_id']
            date_of_joining = form.cleaned_data['date_of_joining']
            
            # Calculate years of experience
            current_date = datetime.now().date()
            experience_years = (current_date - date_of_joining).days / 365
            
            # Determine if eligible for promotion
            eligible = experience_years > 5
            
            return render(request, 'promotion_eligibility.html', {
                'form': form,
                'eligible': eligible,
                'employee_id': employee_id,
            })
    else:
        form = PromotionEligibilityForm()

    return render(request, 'promotion_eligibility.html', {'form': form})

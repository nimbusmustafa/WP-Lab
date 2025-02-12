from django import forms

class PromotionEligibilityForm(forms.Form):
    EMPLOYEE_CHOICES = [
        ('E001', 'Employee 001'),
        ('E002', 'Employee 002'),
        ('E003', 'Employee 003'),
        ('E004', 'Employee 004'),
        ('E005', 'Employee 005'),
    ]
    
    employee_id = forms.ChoiceField(choices=EMPLOYEE_CHOICES, label='Select Employee ID')
    date_of_joining = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Date of Joining')

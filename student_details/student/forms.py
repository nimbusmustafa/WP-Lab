from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Enter student name', 'class': 'form-control'})
    )
    dob = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    address = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter student address', 'class': 'form-control', 'rows': 4}),
        max_length=300
    )
    contact_number = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder': 'Enter contact number', 'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Enter email address', 'class': 'form-control'})
    )
    english_marks = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter English marks (0-100)', 'class': 'form-control'})
    )
    physics_marks = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Physics marks (0-100)', 'class': 'form-control'})
    )
    chemistry_marks = forms.IntegerField(
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={'placeholder': 'Enter Chemistry marks (0-100)', 'class': 'form-control'})
    )

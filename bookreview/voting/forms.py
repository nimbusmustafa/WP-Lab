from django import forms
from .models import BookVote

class VoteForm(forms.ModelForm):
    class Meta:
        model = BookVote
        fields = ['vote']
        widgets = {
            'vote': forms.RadioSelect
        }

from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['issue', 'name', 'photo']
        widgets = {
            'issue': forms.Textarea(attrs={
                'rows': 5, 
                'placeholder': 'Describe your issue here...'
            }),
            'name': forms.TextInput(attrs={
                'placeholder': 'Your Name (optional)'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'accept': 'image/*',
                'capture': 'environment',
                'placeholder': 'Attach a photo (optional)'
            }),
        }

from django import forms
from .models import MessageContact

class ContactForm(forms.ModelForm):
    class Meta:
        model = MessageContact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Votre nom'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'nom@example.com'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Votre message...', 'rows': 5}),
        }

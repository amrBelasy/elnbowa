from django import forms
from .models import ContactFormModel, HomeImage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactFormModel
        fields = ['الاسم', 'الرقم', 'الوصف']




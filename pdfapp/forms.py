# pdfapp/forms.py
from django import forms
from .models import PDFDocument  # Update the import to use the correct model name

class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = PDFDocument  # Update the model reference
        fields = ['file']
        
        

class UploadPDFForm(forms.ModelForm):
    class Meta:
        model = PDFDocument
        fields = ['user_provided_name', 'file']

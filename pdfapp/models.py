# pdfapp/models.py
from django.db import models

class PDFDocument(models.Model):  # Change the class name to 'PDFDocument'
    file = models.FileField(upload_to='documents/')  # Adjust 'documents/' to your desired upload path
    
class PDFDocument(models.Model):
    user_provided_name = models.CharField(max_length=255, default='No_Name')
    file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.file.name

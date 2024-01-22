# pdfapp/admin.py
from django.contrib import admin
from .models import PDFDocument  # Update the import to use the correct model name

admin.site.register(PDFDocument)

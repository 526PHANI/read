import os
from tempfile import NamedTemporaryFile
from win32com.client import Dispatch
import pythoncom
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.files.base import ContentFile
import win32com.client
from django.http import JsonResponse

from .models import PDFDocument
from .forms import UploadPDFForm
from .utils import convert_to_pdf
from docx2pdf import convert as convert_docx_to_pdf
from io import BytesIO
import comtypes.client as cc
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials as ServiceAccountCredentials

# ... (other imports)


# ... (other imports)

def upload_pdf(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)

            # Check the file type and convert to PDF if it's a docx file
            if document.file.name.endswith('.docx'):
                docx_content = document.file.read()

                # Save the DOCX content to a temporary file
                with NamedTemporaryFile(delete=False, suffix=".docx") as temp_docx_file:
                    temp_docx_file.write(docx_content)
                    temp_docx_path = temp_docx_file.name

                try:
                    # Initialize COM in the current thread
                    pythoncom.CoInitialize()

                    # Convert the temporary DOCX file to PDF using pywin32
                    convert_docx_to_pdf_with_pywin32(temp_docx_path)
                finally:
                    # Ensure that COM is properly uninitialized
                    pythoncom.CoUninitialize()

                # Read the converted PDF content
                with open(temp_docx_path.replace(".docx", ".pdf"), "rb") as temp_pdf_file:
                    pdf_content = temp_pdf_file.read()

                # Save the converted PDF content to the PDFDocument model
                document.file.save(f"{form.cleaned_data['user_provided_name']}.pdf", ContentFile(pdf_content), save=False)

                # Clean up temporary files
                os.remove(temp_docx_path)
                os.remove(temp_docx_path.replace(".docx", ".pdf"))

            document.save()

            return JsonResponse({'message': 'PDF uploaded successfully'})

    else:
        form = UploadPDFForm()

    pdfs = PDFDocument.objects.all()
    return render(request, 'pdfapp/upload_pdf.html', {'form': form, 'pdfs': pdfs})


def convert_docx_to_pdf_with_pywin32(docx_path):
    word = win32com.client.Dispatch("Word.Application")
    doc = word.Documents.Open(docx_path)
    pdf_path = docx_path.replace(".docx", ".pdf")
    doc.SaveAs(pdf_path, FileFormat=17)  # 17 corresponds to wdFormatPDF
    doc.Close()
    word.Quit()

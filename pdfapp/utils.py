from io import BytesIO
from docx import Document
from reportlab.pdfgen import canvas

def convert_to_pdf(docx_file):
    # Assuming docx_file is a Django InMemoryUploadedFile object
    docx_content = docx_file.read()

    # Load docx content
    doc = Document(BytesIO(docx_content))

    # Create an in-memory buffer for the PDF
    pdf_buffer = BytesIO()

    # Create a ReportLab PDF document
    pdf = canvas.Canvas(pdf_buffer)

    # Iterate through paragraphs in the docx and add them to the PDF
    for paragraph in doc.paragraphs:
        pdf.drawString(100, 800, paragraph.text)
        pdf.showPage()

    # Save the PDF content to the buffer
    pdf_buffer.seek(0)

    return pdf_buffer

# pdfapp/urls.py
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import upload_pdf

urlpatterns = [
    path('', upload_pdf, name='upload_pdf'),
    # Add other URL patterns if needed
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

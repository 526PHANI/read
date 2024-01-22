# FileUploadDemo/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from pdfapp.views import upload_pdf  # Import the upload_pdf view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_pdf, name='upload_pdf'),  # Map the root URL to the upload_pdf view
    path('pdfapp/', include('pdfapp.urls')),
]


# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tuprimera/', include('TuPrimeraPaginaRamirez.urls')),  # <- aquí conectas tu app
]
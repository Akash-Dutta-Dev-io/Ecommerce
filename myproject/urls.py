from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from myapp.views import seller_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', seller_login, name='login'),
    path('', include('myapp.urls')),  
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
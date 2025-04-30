from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from .views import home, register, logout_view
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('logout/', logout_view, name='logout'),
]
if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
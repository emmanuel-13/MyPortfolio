from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from environs import Env


env = Env()
env.read_env()

urlpatterns = [
    path('admin/' + env.str('SECRET_ADMIN_URL'), admin.site.urls, name="admin"),
    path('', include('Frontend.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



handler500 = 'Frontend.views.error_500'
handler404 = 'Frontend.views.error_404'

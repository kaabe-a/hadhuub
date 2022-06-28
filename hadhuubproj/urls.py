from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
# from decouple import config

urlpatterns = [
    path('', include('blog.urls')),
    path('', include('accounts.urls')),
    # path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
	path('ilameerayso/admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import static
from django.urls import include, path

urlpatterns = [
    path('car/', include('main.car.urls')),
    path('access/', include('main.access.urls')),
    path('electronic/', include('main.electronic.urls')),
    path('furniture/', include('main.furniture.urls')),
    path('medical/', include('main.medical.urls')),
    path('mobile/', include('main.mobile.urls')),
    path('ad/', include('main.ad.urls')),
    path('user/', include('main.user.urls')),
    path('image/', include('main.image.urls')),
    path('properties/', include('main.properties.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
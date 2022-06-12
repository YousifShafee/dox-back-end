from django.contrib import admin
from . import settings
from django.contrib.staticfiles.urls import static
from django.urls import include, path

urlpatterns = [
    path('main/car/', include('main.car.urls')),
    path('main/access/', include('main.access.urls')),
    path('main/electronic/', include('main.electronic.urls')),
    path('main/furniture/', include('main.furniture.urls')),
    path('main/medical/', include('main.medical.urls')),
    path('main/mobile/', include('main.mobile.urls')),
    path('main/ad/', include('main.ad.urls')),
    path('main/user/', include('main.user.urls')),
    path('main/image/', include('main.image.urls')),
    path('main/properties/', include('main.properties.urls')),
    path('admin/', admin.site.urls)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
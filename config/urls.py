from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('car/', include('car.urls')),
    path('auth/', include('worker.urls')),
    path('', TemplateView.as_view(template_name='car/index.html'), name='home'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

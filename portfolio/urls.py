from django.contrib import admin
from django.urls import path
from info import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homePage, name='home'),
    path("send-message/", views.send_message_ajax, name="send_message_ajax"),
    
    path('test-debug/', views.test_debug, name='test_debug'),  # New URL for testing DEBUG setting
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path("sensors", views.sensor_list, name='sensor_list' ),
  path("cmd-center", views.command_center, name='cmd-center'),
  path("cmd-submit", views.command_submit, name='cmd-submit'),
  path('add/', views.add_sensor, name='add_sensor'),
  path('delete-sensor/<int:sensor_id>/', views.delete_sensor, name='delete_sensor'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
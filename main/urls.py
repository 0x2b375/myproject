from django.urls import path


from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path("sensors", views.sensor_list, name='sensor_list' ),
  path("cmd-center", views.command_center, name='cmd-center'),
  path("cmd-submit", views.command_submit, name='cmd-submit'),
  path('add/', views.add_sensor, name='add_sensor'),
]
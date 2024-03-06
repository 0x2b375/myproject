from django.urls import path


from . import views

urlpatterns = [
  path("", views.index, name='index'),
  path("/cmd-center", views.command_center, name='cmd-center'),
]
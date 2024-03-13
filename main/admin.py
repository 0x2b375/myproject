from django.contrib import admin
from .models import Sensor
# Register your models here.



class SensorAdmin(admin.ModelAdmin):
  list_display = ["name", "mqtt_topic"]
  

admin.site.register(Sensor, SensorAdmin)
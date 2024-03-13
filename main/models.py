from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

import os
# Create your models here.

class Sensor(models.Model):
  name = models.CharField(max_length=30)
  image = models.ImageField(upload_to='sensor_images/', null=True, blank=True)
  mqtt_topic = models.CharField(max_length=30)
  
  def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

  def __str__(self):
      return self.name
  
  
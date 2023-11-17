from django.db import models
import requests

# Create your models here.

class tiempo_view(models.Model):
    city = models.CharField(max_length=100)
    description = models.TextField()

    def get_weather_data(self):
        api_key = '626901f2caa37bf4341f4bfd6a505f95'
        url = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={api_key}&units=metric&lang=es'

        response = requests.get(url)
        data = response.json()

        self.save()
from django.db import models

class Log(models.Model):
    ip_address = models.GenericIPAddressField()
    timestamp = models.DateTimeField()
    service_name = models.CharField(max_length=255)
    version = models.CharField(max_length=10)
    user_id = models.CharField(max_length=20)
    message = models.TextField()
    level = models.CharField(max_length=50) 
    description = models.TextField()

    def __str__(self):
        return f"{self.timestamp} - {self.service_name} - {self.message}"
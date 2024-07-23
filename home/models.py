from django.db import models

class Application(models.Model):
    tutoring_package = models.CharField(max_length=200)
    service_description = models.TextField()
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=200)

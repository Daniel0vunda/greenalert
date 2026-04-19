from django.db import models

class WasteReport(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField(max_length=2088)
    image = models.ImageField(upload_to='waste_images/', blank=True, null=True)
    status = models.CharField(max_length=100, default='Pending')
    date_submitted = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.location} - {self.status}"
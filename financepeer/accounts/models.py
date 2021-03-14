from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
from django.db import models

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='media/', validators=[FileExtensionValidator(allowed_extensions=['json'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description

class UserData(models.Model):
    # fieldName = models.CharField(max_length = 150)
    userId = models.IntegerField()
    # id = models.IntegerField()
    title = models.CharField(max_length = 300)
    body = models.TextField()

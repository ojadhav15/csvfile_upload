from django.db import models


# Create your models here.
class FileUploadModel(models.Model):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField()
    file = models.FileField(upload_to='filefolder')


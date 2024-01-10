from django.db import models
from django.contrib.auth.models import User


class FileInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_infos")
    path = models.URLField()
    info = models.CharField(max_length=255)


    def __str__(self):
        return self.path
    
class UserFolder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="folders")
    path = models.URLField()

    def __str__(self):
        return self.path

class UserFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="files")
    path = models.URLField()

    def __str__(self):
        return self.path

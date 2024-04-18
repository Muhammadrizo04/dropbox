import os

from django.contrib.auth.models import User

from common.models import BaseModel
from django.db import models
from django.conf import settings


class Folder(BaseModel):
    name = models.CharField(max_length=255)
    parent_folder = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_folder_path(self):
        folder_names = [self.name]
        current_folder = self.parent_folder
        while current_folder is not None:
            folder_names.insert(0, current_folder.name)
            current_folder = current_folder.parent_folder
        folder_names.insert(0, str(self.owner.username))
        return os.path.join(settings.MEDIA_ROOT, *folder_names)

    def save(self, *args, **kwargs):
        super(Folder, self).save(*args, **kwargs)
        user_folder = self.get_folder_path()
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

    def __str__(self) -> str:
        return self.name


class File(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='uploads/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

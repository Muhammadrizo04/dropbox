import os
import shutil

from django.contrib.auth.models import User
from django.urls import reverse

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

    def get_subfolders(self):
        return self.folder_set.all()

    def get_absolute_url(self):
        return reverse('open_folder', kwargs={'guid': self.guid})

    def get_parent_folder_url(self):
        if self.parent_folder:
            return self.parent_folder.get_absolute_url()
        return None

    def delete_folder(self):
        try:
            folder_path = self.get_folder_path()
            if os.path.exists(folder_path):
                shutil.rmtree(folder_path)
            self.delete()
            return True
        except Exception as e:
            return False

    def get_all_parent_folders(self):
        parent_folders = []
        current_folder = self.parent_folder
        while current_folder is not None:
            parent_folders.insert(0, current_folder)
            current_folder = current_folder.parent_folder
        return parent_folders[:-1]

    def rename_folder(self, new_name):
        old_name = self.name
        self.name = new_name
        try:
            self.save()
            old_path = self.get_folder_path()
            new_path = self.get_folder_path()
            if os.path.exists(old_path):
                os.rename(old_path, new_path)
            return True
        except Exception as e:
            self.name = old_name
            self.save()
            return False

    @classmethod
    def create_folder(cls, name, parent_folder=None, owner=None):
        folder = cls(name=name, parent_folder=parent_folder, owner=owner)
        folder.save()
        return folder

    def save(self, *args, **kwargs):
        super(Folder, self).save(*args, **kwargs)
        user_folder = self.get_folder_path()
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

    def __str__(self) -> str:
        return self.name


class File(BaseModel):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='temp/', null=True, blank=True)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

    def move(self):
        old_file_path = self.file.path
        if os.path.exists(old_file_path):
            new_file_path = os.path.join(self.folder.get_folder_path(), self.name)
            os.rename(old_file_path, new_file_path)

            print(f"File '{self.name}' moved to '{new_file_path}'")

            if os.path.exists(old_file_path):
                os.remove(old_file_path)
                print("Old file removed")
            else:
                print("Old file does not exist")
        else:
            print(f"File '{old_file_path}' does not exist")

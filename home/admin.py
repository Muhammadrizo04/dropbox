from django.contrib import admin
from home.models import FileInfo, UserFile, UserFolder

# Register your models here.

admin.site.register(FileInfo)
admin.site.register(UserFile)
admin.site.register(UserFolder)
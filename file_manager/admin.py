from django.contrib import admin
from .models import Folder, File


class ReadOnlyAdminMixin:
    """Mixin to make admin view read-only"""

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Folder)
class FolderAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'owner']
    readonly_fields = ['name', 'owner']


@admin.register(File)
class FileAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'folder', 'owner']
    readonly_fields = ['name', 'folder', 'owner']

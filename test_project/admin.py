from django.contrib import admin

from test_project import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Note)
class NoteAdmin(admin.ModelAdmin):
    pass

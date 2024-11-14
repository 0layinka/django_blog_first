from django.contrib import admin
from . import models
# Register your models here.

@admin.register(models.Posts)
class postAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
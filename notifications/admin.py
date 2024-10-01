from django.contrib import admin
from . import models

#Admin
@admin.register(models.Notification)
class CustomQuestionAdmin(admin.ModelAdmin):
    pass

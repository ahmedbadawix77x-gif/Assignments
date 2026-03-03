from django.contrib import admin

from .models import models.Event  # تأكد من كتابة اسم الموديل الخاص بك هنا

admin.site.register(models.Event)
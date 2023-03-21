from django.contrib import admin
from .models import Payload, AttachFile

# Register your models here.

admin.site.register(Payload)
admin.site.register(AttachFile)

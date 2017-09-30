from django.contrib import admin
from .models import Fan
# Register your models here.
class FanAdmin(admin.ModelAdmin):
    pass
admin.site.register(Fan, FanAdmin)

from django.contrib import admin
from startups import models

# Register your models here.
admin.site.register(models.Startup)
admin.site.register(models.ReadinessLevel)

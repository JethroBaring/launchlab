from django.contrib import admin
from users import models

# Register your models here.
admin.site.register(models.BaseUser)
admin.site.register(models.ManagerUser)
admin.site.register(models.StartupUser)

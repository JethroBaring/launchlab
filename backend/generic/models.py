from django.db import models


class BaseModel(models.Model):
    datetime_updated = models.DateTimeField(auto_now=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_deleted = models.DateTimeField(default=None, null=True)

    class Meta:
        abstract = True

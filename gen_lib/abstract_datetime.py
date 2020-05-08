from django.db import models


class DateTimeRecord(models.Model):
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


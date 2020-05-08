from django.contrib.auth.models import User
from django.db import models


class UserRecord(models.Model):

    user_creation = \
        models.ForeignKey(User, db_column='user_creation_fk',
                          verbose_name='User Creation',
                          on_delete=models.PROTECT,
                          related_name='%(app_label)s_%(class)s_creation',
                          blank=True, null=True, db_index=True)
    user_modified = \
        models.ForeignKey(User, db_column='user_modified_fk',
                          verbose_name='User Modified',
                          on_delete=models.PROTECT,
                          related_name='%(app_label)s_%(class)s_modified',
                          blank=True, null=True, db_index=True)

    class Meta:
        abstract = True



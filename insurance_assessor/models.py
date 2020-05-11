from django.contrib.auth.models import User
from django.db import models

from gen_lib.abstract_datetime import DateTimeRecord
from gen_lib.abstract_user import UserRecord


class Assessor(DateTimeRecord, UserRecord):
    name = models.CharField('Name', db_column='name', max_length=50,
                            db_index=True)
    phone_number = models.CharField('Phone Number', db_column='phone_number',
                                    max_length=15, blank=True, null=True)
    linked_user = models.OneToOneField(User, db_column='linked_user_fk',
                                    verbose_name='Linked User', unique=True,
                                    on_delete=models.PROTECT, db_index=True,
                                    related_name='assessor_linked_user'
                                  )

    class Meta:
        db_table = 'assessor'
        unique_together = ('name', 'linked_user')
        ordering = ['name']

    def __str__(self):
        return "{} [{}]".format(self.name, self.linked_user.username)

    def __unicode__(self):
        return "{} [{}]".format(self.name, self.linked_user.username)

    def phone_number_valid(self):
        from gen_lib.utils import strip_non_ascii, strip_non_numeric

        temp_phone_number = self.phone_number.replace('(', '')
        temp_phone_number = temp_phone_number.replace(')', '')
        temp_phone_number = temp_phone_number.replace('+', '')
        temp_phone_number = strip_non_ascii(temp_phone_number)
        temp_phone_number = strip_non_numeric(temp_phone_number)
        return temp_phone_number

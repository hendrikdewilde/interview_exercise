from django.contrib.auth.models import User
from django.db import models

from gen_lib.abstract_datetime import DateTimeRecord
from gen_lib.abstract_user import UserRecord


class Insurance(DateTimeRecord, UserRecord):
    name = models.CharField('Name', db_column='name', unique=True,
                            max_length=50, db_index=True)
    phone_number = models.CharField('Phone Number', db_column='phone_number',
                                    max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'insurance'
        ordering = ['name']

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name


class InsuranceConsultant(DateTimeRecord, UserRecord):
    name = models.CharField('Name', db_column='name', max_length=50,
                            db_index=True)
    phone_number = models.CharField('Phone Number', db_column='phone_number',
                                    max_length=15, blank=True, null=True)
    insurance = models.ForeignKey(Insurance, db_column='insurance_fk',
                                  verbose_name='Insurance',
                                  on_delete=models.PROTECT, db_index=True,
                                  related_name='insurance_consultant_insurance'
                                  )
    linked_user = models.OneToOneField(User, db_column='linked_user_fk',
                                    verbose_name='Linked User', unique=True,
                                    on_delete=models.PROTECT, db_index=True,
                                    related_name='insurance_consultant_linked_user'
                                    )

    class Meta:
        db_table = 'insurance_consultant'
        unique_together = ('name', 'insurance')
        ordering = ['insurance', 'name']

    def __str__(self):
        return "{} [{}]".format(self.name, self.insurance.name)

    def __unicode__(self):
        return "{} [{}]".format(self.name, self.insurance.name)


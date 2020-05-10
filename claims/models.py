import logging
from datetime import datetime

from django.db import models

from claims.defines import CASE_STATUS, CASE_DOCUMENT_TYPE
from gen_lib.abstract_datetime import DateTimeRecord
from gen_lib.abstract_user import UserRecord
from insurance_assessor.models import Assessor
from insurance_companies.models import Insurance, InsuranceConsultant
from interview_exercise.settings import MEDIA_ROOT

log = logging.getLogger(__name__)


class Client(DateTimeRecord, UserRecord):
    client_number = models.IntegerField('Client Number',
                                        db_column='client_number',
                                        db_index=True, unique=True)
    name = models.CharField('Name', db_column='name', max_length=50)
    phone_number = models.CharField('Phone Number', db_column='phone_number',
                                    max_length=15, blank=True, null=True)
    address = models.TextField('Address', db_column='address', blank=True,
                               null=True)

    class Meta:
        db_table = 'client'
        ordering = ['client_number']

    def __str__(self):
        return "{} [{}]".format(self.name, self.client_number)

    def __unicode__(self):
        return "{} [{}]".format(self.name, self.client_number)


class Case(DateTimeRecord, UserRecord):
    case_number = models.CharField('Case Number', db_column='case_number',
                                   max_length=50, unique=True, db_index=True)
    status = models.CharField('Status', db_column='status', max_length=10,
                              choices=CASE_STATUS)
    open_date = models.DateField('Open Date', db_column='open_date')
    close_date = models.DateField('Close Date', db_column='close_date',
                                  blank=True, null=True)
    insurance = models.ForeignKey(Insurance, db_column='insurance_fk',
                                  verbose_name='Insurance',
                                  on_delete=models.PROTECT, db_index=True,
                                  related_name='case_insurance'
                                  )
    insurance_consultant = models.ForeignKey(InsuranceConsultant,
                                             db_column='insurance_consultant_fk',
                                             verbose_name='Insurance Consultant',
                                             on_delete=models.PROTECT,
                                             db_index=True,
                                             related_name='case_insurance_consultant'
                                             )
    assessor = models.ForeignKey(Assessor, db_column='assessor_fk',
                                 verbose_name='Assessor',
                                 on_delete=models.PROTECT, db_index=True,
                                 related_name='case_assessor'
                                 )
    client = models.ForeignKey(Client, db_column='client_fk',
                               verbose_name='Client',
                               on_delete=models.PROTECT, db_index=True,
                               related_name='case_client'
                               )
    description = models.TextField('Description', db_column='description',
                                   blank=True, null=True)
    resolution = models.TextField('Resolution', db_column='resolution',
                                  blank=True, null=True)

    class Meta:
        db_table = 'case'
        ordering = ['case_number']

    def __str__(self):
        return "{} [{}] ({})".format(self.case_number, self.insurance.name,
                                     self.assessor.name)

    def __unicode__(self):
        return "{} [{}] ({})".format(self.case_number, self.insurance.name,
                                     self.assessor.name)

    def get_dir_path(self):
        # Local store Dir
        import os
        directory = "{}/{}".format(MEDIA_ROOT, self.case_number)
        if not os.path.exists(directory):
            try:
                os.makedirs(directory)
            except OSError as err:
                log.error(err)
        return directory

    def case_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/case_number/20200507/<filename>
        today_date = datetime.now()
        today_date_str = today_date.strftime("%Y%m%d%H%M%S")
        return '{0}/{1}/{2}'.format(instance.case.case_number, today_date_str,
                                    filename)


class Document(DateTimeRecord, UserRecord):
    document_type = models.CharField('Document Type',
                                     db_column='document_type', max_length=50,
                                     choices=CASE_DOCUMENT_TYPE)
    name = models.CharField('Name', db_column='name', max_length=50)
    file_name = models.FileField(upload_to=Case.case_directory_path)
    case = models.ForeignKey(Case, db_column='case_fk',
                             verbose_name='Case',
                             on_delete=models.PROTECT, db_index=True,
                             related_name='document_case'
                             )

    class Meta:
        db_table = 'document'
        ordering = ['case', 'id']

    def __str__(self):
        return "{} - {} [{}]".format(self.name, self.document_type,
                                     self.case.case_number)

    def __unicode__(self):
        return "{} - {} [{}]".format(self.name, self.document_type,
                                     self.case.case_number)


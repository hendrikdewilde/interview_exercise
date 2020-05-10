import logging

from django.contrib.auth.models import User
from django.contrib.postgres.fields import JSONField
from django.db import models

from gen_lib.abstract_datetime import DateTimeRecord

log = logging.getLogger(__name__)


class StreamLogging(DateTimeRecord):
    level = models.CharField(max_length=255, blank=True, null=True)
    traceback = models.TextField(blank=True, null=True)
    error_time = models.DateTimeField(auto_now_add=True)
    file_name = models.CharField(max_length=255, blank=True, null=True)
    func_name = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    process_id = models.CharField(max_length=255, blank=True, null=True)
    process_name = models.CharField(max_length=255, blank=True, null=True)
    process_args = models.CharField(max_length=255, blank=True, null=True)
    ip_address = models.CharField('IP', db_column='ip', max_length=255,
                                  blank=True, null=True)

    class Meta:
        db_table = 'stream_logging'
        ordering = ['-date_creation']

    def __str__(self):
        return self.message

    def __unicode__(self):
        return self.message


class UserLogging(DateTimeRecord):
    user = models.ForeignKey(User, db_column='user_fk', verbose_name='User',
                             on_delete=models.PROTECT, db_index=True,
                             blank=True, null=True,
                             related_name='user_login_user')
    username = models.CharField('UserName', db_column='username',
                                max_length=255, blank=True, null=True)
    session_id = models.CharField('Session ID', max_length=45,
                                  db_column='session_id', blank=True,
                                  null=True)
    access_token = models.CharField('Access Token', max_length=45,
                                    db_column='access_token', blank=True,
                                    null=True)
    ip_address = models.CharField('IP Address', max_length=255,
                                  db_column='ip_address', blank=True,
                                  null=True)
    host = models.CharField('Host', db_column='host', max_length=255,
                            blank=True, null=True)
    success = models.BooleanField('Success', db_column='success', blank=True,
                            default=False)

    class Meta:
        db_table = 'user_login'
        ordering = ['-date_creation']

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class ApiLogging(DateTimeRecord):
    user = models.ForeignKey(User, db_column='user_fk', verbose_name='User',
                             on_delete=models.PROTECT, db_index=True,
                             blank=True, null=True,
                             related_name='api_logging_user')
    status = models.CharField('Status', db_column='status', max_length=5,
                              db_index=True, blank=True, null=True)
    method = models.CharField('Method', db_column='method', max_length=50,
                              blank=True, null=True)
    path = models.CharField('Path', db_column='path', max_length=255,
                            blank=True, null=True)
    ip_address = models.CharField('IP', db_column='ip', max_length=255,
                                  blank=True, null=True)
    host = models.CharField('Host', db_column='host', max_length=255,
                            blank=True, null=True)
    cookie = models.CharField('Cookie', max_length=255, db_column='cookie',
                              blank=True, null=True)
    params = JSONField('Params', db_column='params', blank=True, null=True)

    class Meta:
        db_table = 'api_logging'
        ordering = ['-date_creation']

    def __str__(self):
        return self.path

    def __unicode__(self):
        return self.path

    @staticmethod
    def log_api_request(self, request=None):
        from gen_lib.utils import get_client_ip, get_user_request

        user_obj = get_user_request(request)

        method = None
        path = None
        host = None
        params = None
        cookie = None
        status = None
        if request:
            method = request.method
            path = request.path
            host = request.META.get('HTTP_HOST')
            params = request.META.get('QUERY_STRING')
            cookie = request.META.get('HTTP_COOKIE')
            if cookie is None:
                cookie = request.META.get('HTTP_AUTHORIZATION')

        # save log_data in some way
        log_obj = self(
            user=user_obj or None,
            status=status,
            method=method,
            path=path,
            ip_address=get_client_ip(request) or None,
            host=host,
            cookie=cookie,
            params=params
        )
        log_obj.save()
        return log_obj.id

    @staticmethod
    def log_api_response(self, log_id=None, response=None):
        if log_id and response:
            status = response.status_code

            try:
                log_obj = self.objects.get(id=log_id)
            except self.DoesNotExist:
                return False
            else:
                # save log_data in some way
                log_obj.status = status
                log_obj.save()
                return True
        else:
            return False


class SmsLogging(DateTimeRecord):
    user = models.ForeignKey(User, db_column='user_fk', verbose_name='User',
                             on_delete=models.PROTECT, db_index=True,
                             blank=True, null=True,
                             related_name='sms_logging_user')
    from_number = models.CharField('From number', max_length=15,
                                    db_column='from_number', blank=True,
                                    null=True)
    to_number = models.CharField('To number', max_length=15,
                                  db_column='to_number', blank=True,
                                  null=True)
    message = models.CharField('Message', db_column='message', max_length=255,
                            blank=True, null=True)
    sms_id = models.CharField('SMS Id', db_column='sms_id', max_length=255,
                            blank=True, null=True)

    class Meta:
        db_table = 'sms_logging'
        ordering = ['-date_creation']

    def __str__(self):
        return self.to_number

    def __unicode__(self):
        return self.to_number

    @staticmethod
    def send_sms(self, number, text_message, user_obj=None):
        from twilio.rest import Client
        from interview_exercise.settings import TWILLIO_ACCOUNT, \
            TWILLIO_AUTH_TOKEN, TWILLIO_FROM_NUMBER

        if text_message not in [None, ""] and number not in [None, ""]:
            try:
                client = Client(TWILLIO_ACCOUNT, TWILLIO_AUTH_TOKEN)
            except Exception as err:
                log.error(err)
            else:
                sms_message = client.messages.create(
                    body=text_message,
                    from_=TWILLIO_FROM_NUMBER,
                    to=number
                )

                sms_id = None
                if sms_message.sid:
                    sms_id = sms_message.sid

                log_obj = self(
                    user=user_obj,
                    from_number=TWILLIO_FROM_NUMBER,
                    to_number=number,
                    message=text_message,
                    sms_id=sms_id
                )
                log_obj.save()


class BlockIP(DateTimeRecord):
    ip_address = models.CharField('IP Address', max_length=255,
                                  db_column='ip_address', unique=True)
    reason_for_block = models.TextField(blank=True, null=True,
                                        help_text="Optional reason for block")

    def __str__(self):
        return 'BlockIP: %s' % self.ip_address

    class Meta:
        verbose_name = 'IPs to ban'
        db_table = 'block_ip'
        ordering = ['-date_creation']


class SafeIP(DateTimeRecord):
    ip_address = models.CharField('IP Address', max_length=255,
                                  db_column='ip_address', unique=True)
    reason_for_allow = models.TextField(blank=True, null=True,
                                        help_text="Optional reason to always "
                                                  "Allow")

    def __str__(self):
        return 'SafeIP: %s' % self.ip_address

    class Meta:
        verbose_name = 'IPs to always Allow'
        db_table = 'save_ip'
        ordering = ['-date_creation']

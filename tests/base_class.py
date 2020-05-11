from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import TestCase, Client as TestClient
from django.test.client import RequestFactory
from django.urls import reverse

from claims.admin import CaseAdmin, ClientAdmin, DocumentAdmin
from claims.models import Case, Client, Document
from insurance_assessor.admin import AssessorAdmin
from insurance_assessor.models import Assessor
from insurance_companies.admin import InsuranceConsultantAdmin, InsuranceAdmin
from insurance_companies.models import InsuranceConsultant, Insurance
from logs.admin import StreamLoggingAdmin, UserLoggingAdmin, ApiLoggingAdmin, \
    SmsLoggingAdmin, BlockIPAdmin, SafeIPAdmin
from logs.models import StreamLogging, UserLogging, ApiLogging, SmsLogging, \
    BlockIP, SafeIP


class MockSuperUser:
    def has_perm(self, perm):
        return True


class MockRequest(object):
    def __init__(self, user=None):
        self.user = user


def get_admin_change_view_url(obj: object) -> str:
    return reverse(
        'admin:{}_{}_change'.format(
            obj._meta.app_label,
            type(obj).__name__.lower()
        ),
        args=(obj.pk,)
    )


class BaseTestCase(TestCase):
    """
    Will use django.test
    With sqlite3 - remember it only do migrations for initial and not other
    migrations after initial. It is a bug
    """
    # Add test functionality for admin site
    request_factory = RequestFactory()
    request = request_factory.get('/admin')
    request.user = MockSuperUser()

    # If you need to test something using messages
    setattr(request, 'session', 'session')
    messages = FallbackStorage(request)
    setattr(request, '_messages', messages)

    def setUp(self):
        # Setup run before every test method.
        # Create all Admin views
        site = AdminSite()
        self.log_stream_admin = StreamLoggingAdmin(StreamLogging, site)
        self.log_user_admin = UserLoggingAdmin(UserLogging, site)
        self.log_api_admin = ApiLoggingAdmin(ApiLogging, site)
        self.log_sms_admin = SmsLoggingAdmin(SmsLogging, site)
        self.log_block_admin = BlockIPAdmin(BlockIP, site)
        self.log_save_admin = SafeIPAdmin(SafeIP, site)
        self.insurance_companies_admin = InsuranceAdmin(Insurance, site)
        self.insurance_consultant_admin = InsuranceConsultantAdmin(
            InsuranceConsultant, site)
        self.insurance_assessor_admin = AssessorAdmin(Assessor, site)
        self.claims_case_admin = CaseAdmin(Case, site)
        self.claims_client_admin = ClientAdmin(Client, site)
        self.claims_document_admin = DocumentAdmin(Document, site)

        # Add users to test with
        self.super_user = User.objects.create_superuser(username='super',
                                                   email='super@email.org',
                                                   password='pass')
        self.user1 = User.objects.create(username="user1", email="user1@mail.co.za")
        self.user2 = User.objects.create(username="user2", email="user2@mail.co.za")
        self.user3 = User.objects.create(username="user3", email="user3@mail.co.za")

        self.client = TestClient()
        self.client.force_login(user=self.super_user)

    def tearDown(self):
        # Clean up run after every test method.
        pass



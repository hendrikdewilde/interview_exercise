from django.contrib.auth.models import Group

from tests.base_class import BaseTestCase, get_admin_change_view_url


class AdminTestCase(BaseTestCase):
    def get_instance_assessors(self):
        instance, _ = Group.objects.get_or_create(name='Assessors')
        return instance

    def get_instance_insurance_consultant(self):
        instance, _ = Group.objects.get_or_create(name='InsuranceConsultant')
        return instance

    # Test Default Admin Groups
    def test_change_view_loads_normally_assessors(self):
        instance = self.get_instance_assessors()
        response = self.client.get(get_admin_change_view_url(instance))
        self.assertEqual(response.status_code, 200)

    def test_change_view_loads_normally_insurance_consultant(self):
        instance = self.get_instance_insurance_consultant()
        response = self.client.get(get_admin_change_view_url(instance))
        self.assertEqual(response.status_code, 200)

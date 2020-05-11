from insurance_companies.models import Insurance, InsuranceConsultant
from tests.base_class import BaseTestCase, MockRequest


class InsuranceTestCase(BaseTestCase):

    def create_insurance(self):
        return Insurance.objects.create(name="AA Insurance",
                                               phone_number="01234567890")

    def create_consultant_1(self):
        insurance = self.create_insurance()
        return InsuranceConsultant.objects.create(name="Pieter",
                                                  phone_number="01234567890",
                                                  insurance=insurance,
                                                  linked_user=self.user1)

    def create_consultant_2(self):
        insurance = self.create_insurance()
        return InsuranceConsultant.objects.create(name="Bennie",
                                                  phone_number="01234567890",
                                                  insurance=insurance,
                                                  linked_user=self.user2)

    def test_insurance_creation(self):
        w = self.create_insurance()
        self.assertTrue(isinstance(w, Insurance))
        self.assertEqual(w.__unicode__(), "{}".format(w.name))
        aa = Insurance.objects.get(name="AA Insurance")
        self.assertEqual(aa.phone_number, '01234567890')

    def test_consultant_creation_1(self):
        w = self.create_consultant_1()
        self.assertTrue(isinstance(w, InsuranceConsultant))
        self.assertEqual(w.__unicode__(), "{} [{}]".format(w.name,
                                                           w.insurance.name))
        pieter = InsuranceConsultant.objects.get(name="Pieter")
        self.assertEqual(pieter.phone_number, '01234567890')

    def test_consultant_creation_2(self):
        w = self.create_consultant_2()
        self.assertTrue(isinstance(w, InsuranceConsultant))
        self.assertEqual(w.__unicode__(), "{} [{}]".format(w.name,
                                                           w.insurance.name))
        bennie = InsuranceConsultant.objects.get(name="Bennie")
        self.assertEqual(bennie.phone_number, '01234567890')

    def test_admin_companies_add_model(self):
        self.insurance_companies_admin.save_model(
            obj=Insurance(name="AA", phone_number="0123456789"),
            request=MockRequest(user=self.super_user),
            form={}, change=None)
        added = Insurance.objects.filter(name="AA").first()
        self.assertEqual(added.name, "AA")

    def test_admin_companies_delete_model(self):
        w = self.create_insurance()
        obj = Insurance.objects.get(name="AA Insurance")
        self.insurance_companies_admin.delete_model(self.request, obj)

        deleted = Insurance.objects.filter(name="AA Insurance").first()
        self.assertEqual(deleted, None)

    def test_admin_consultant_add_model(self):
        insurance = self.create_insurance()
        self.insurance_consultant_admin.save_model(
            obj=InsuranceConsultant(name="test1",
                                    phone_number="0123456789",
                                    insurance=insurance,
                                    linked_user=self.user1),
            request=MockRequest(user=self.super_user),
            form={}, change=None)
        added = InsuranceConsultant.objects.filter(name="test1").first()
        self.assertEqual(added.name, "test1")

    def test_admin_consultant_delete_model(self):
        w = self.create_consultant_1()
        obj = InsuranceConsultant.objects.get(name="Pieter")
        self.insurance_consultant_admin.delete_model(self.request, obj)

        deleted = InsuranceConsultant.objects.filter(name="Pieter").first()
        self.assertEqual(deleted, None)


from insurance_assessor.models import Assessor
from tests.base_class import BaseTestCase, MockRequest


class AssessorTestCase(BaseTestCase):

    def create_assessor_1(self):
        return Assessor.objects.create(name="Ben",
                                       phone_number="(012)34567890",
                                       linked_user=self.user1)

    def create_assessor_2(self):
        return Assessor.objects.create(name="Koos",
                                       phone_number="+01234567890",
                                       linked_user=self.user2)

    def create_assessor_3(self):
        return Assessor.objects.create(name="Sannie",
                                       phone_number="A1234567890",
                                       linked_user=self.user1)

    def test_assessor_creation_1(self):
        w = self.create_assessor_1()
        self.assertTrue(isinstance(w, Assessor))
        self.assertEqual(w.__unicode__(), "{} [{}]".format(w.name,
                                                           w.linked_user.username))
        ben = Assessor.objects.get(name="Ben")
        self.assertEqual(ben.phone_number_valid(), '01234567890')

    def test_assessor_creation_2(self):
        w = self.create_assessor_2()
        self.assertTrue(isinstance(w, Assessor))
        self.assertEqual(w.__unicode__(), "{} [{}]".format(w.name,
                                                           w.linked_user.username))
        koos = Assessor.objects.get(name="Koos")
        self.assertEqual(koos.phone_number_valid(), '01234567890')

    def test_assessor_creation_3(self):
        w = self.create_assessor_3()
        self.assertTrue(isinstance(w, Assessor))
        self.assertEqual(w.__unicode__(), "{} [{}]".format(w.name,
                                                           w.linked_user.username))
        sannie = Assessor.objects.get(name="Sannie")
        self.assertEqual(sannie.phone_number_valid(), '1234567890')

    def test_admin_add_model(self):
        self.insurance_assessor_admin.save_model(
            obj=Assessor(name="test1", phone_number="0123456789", linked_user=self.user1),
            request=MockRequest(user=self.super_user),
            form={}, change=None)
        added = Assessor.objects.filter(name="test1").first()
        self.assertEqual(added.name, "test1")

    def test_admin_delete_model(self):
        w = self.create_assessor_1()
        obj = Assessor.objects.get(name="Ben")
        self.insurance_assessor_admin.delete_model(self.request, obj)

        deleted = Assessor.objects.filter(name="Ben").first()
        self.assertEqual(deleted, None)


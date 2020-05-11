from django.contrib.auth.models import User
from insurance_assessor.models import Assessor
from tests.base_class import BaseTestCase
from django.test import Client


class AssessorTestCase(BaseTestCase):

    def create_assessor_1(self):
        user_obj_1 = User.objects.get(username="user1")
        return Assessor.objects.create(name="Ben",
                                       phone_number="(012)34567890",
                                       linked_user=user_obj_1)

    def create_assessor_2(self):
        user_obj_2 = User.objects.get(username="user2")
        return Assessor.objects.create(name="Koos",
                                       phone_number="+01234567890",
                                       linked_user=user_obj_2)

    def create_assessor_3(self):
        user_obj_3 = User.objects.get(username="user3")
        return Assessor.objects.create(name="Sannie",
                                       phone_number="A1234567890",
                                       linked_user=user_obj_3)

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

    # def test_view(self):
    #     c = Client()
    #     response = c.get('/admin/insurance_assessor/assessor/')
    #
    #     self.assertEqual(response.status_code, 200)
    #
    #     self.assertEqual(response.content, b'<!DOCTYPE html...')




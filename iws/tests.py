from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from iws.models import Field, RiskType

class APiTest(APITestCase):
    def setUp(self):
        self.field = Field.objects.create(
            field_name='test', data_type="enum")
        self.risktype = RiskType.objects.create(
            name='test')

    def test_get_field_list(self):
        """
        Ensure we can get list of fields.
        """
        url = reverse('get_post_field')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_field_list(self):
        """
        Ensure we can create list of field object.
        """
        url = reverse('get_post_field')
        data = [{'field_name': 'field test', 'data_type': 'enum'}]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail_field(self):
        """
        Ensure we can retrieve singe field object by id
        """
        url = reverse('field_detail', kwargs={'pk': self.field.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_risktype_list(self):
        """
        Ensure we can get a list of risktypes.
        """
        url = reverse('get_post_risktype')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_risktype_list(self):
        """
        Ensure we can create list of risktype object.
        """
        url = reverse('get_post_risktype')
        data = [{'name': 'test risktype'}]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_detail_risktype(self):
        """
        Ensure we can retrieve singe risktype by id
        """
        url = reverse('get_detail_risktype', kwargs={'pk': self.risktype.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
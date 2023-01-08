from rest_framework.test import APIClient, APITestCase
from .models import Template
from rest_framework import status
from .serializers import TemplateValidationSerializer


class TemplateApiTest(APITestCase):
    def test_valid_request(self):
        Template.objects.create(
            name="some_name",
            email="em1aidf.sd",
            phone="+79718830255",
            date="2022-2-2",
            text="some",
        )

        data = {
            "name": "some_name",
            "email": "some@em1aidf.sd",
            "phone": "+79718830255",
            "date": "2022.2.2",
            "text": "some_text",
        }
        client = APIClient()
        response = client.post("/get_form/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_request(self):
        Template.objects.create(
            name="some_name",
            email="em1aidf.sd",
            phone="+79718830255",
            date="2022-2-2",
            text="some",
        )

        data = {
            "name": "invalid_name",
            "email": "some@em1aidf.sd",
            "phone": "+79718830255",
            "date": "2022.2.2",
            "text": "some_text",
        }
        client = APIClient()
        response = client.post("/get_form/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_validation_serializer(self):
        data1 = {
            "name": "invalid_name",
            "email": "some@em1aidf.ryyyq",
            "phone": "+7(971)830-25-45",
            "date": "2022.2.2",
            "text": "some_text",
        }
        ser1 = TemplateValidationSerializer(data=data1)

        data2 = {
            "name": "invalid_name",
            "email": "gdgdfgdfg@sdfsdf",
            "phone": "+7(971)830-22225-45-1",
            "date": "2022.2.222",
            "text": "some_text",
        }

        ser2 = TemplateValidationSerializer(data=data2)
        self.assertIs(ser1.is_valid(), True)
        self.assertIs(ser2.is_valid(), False)
        self.assertEqual(len(ser2.errors), 3)

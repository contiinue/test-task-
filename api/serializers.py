from rest_framework import serializers
from formvalidation.settings import DATE_INPUT_FORMATS
from phonenumber_field.serializerfields import PhoneNumberField


class TemplateValidationSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=63)
    email = serializers.EmailField()
    date = serializers.DateField(input_formats=DATE_INPUT_FORMATS)
    phone = PhoneNumberField()
    text = serializers.CharField(max_length=270)

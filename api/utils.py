from .models import Template
from .serializers import TemplateValidationSerializer
from django.core.exceptions import ObjectDoesNotExist
from dataclasses import dataclass
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_200_OK


@dataclass
class TemplateData:
    data: dict
    status: HTTP_200_OK | HTTP_204_NO_CONTENT


def get_template(data: TemplateValidationSerializer) -> TemplateData:
    try:
        qs: Template = Template.objects.get(name=data.validated_data["name"])
        return TemplateData(data={"name": qs.name}, status=HTTP_200_OK)
    except ObjectDoesNotExist:
        return TemplateData(
            data={"name": "шаблон не найден"}, status=HTTP_204_NO_CONTENT
        )

from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TemplateValidationSerializer
from .utils import get_template


class TemplateValidation(APIView):
    def post(self, request):
        form = TemplateValidationSerializer(data=request.data)
        form.is_valid(raise_exception=True)
        template = get_template(form)
        return Response(data=template.data, status=template.status)

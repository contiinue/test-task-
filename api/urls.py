from django.urls import path
from .views import TemplateValidation


urlpatterns = [path("get_form/", TemplateValidation.as_view())]

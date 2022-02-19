from xml.etree.ElementInclude import include
from django import views
from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, ProductViewSet, schema_view
from django.views.generic import TemplateView

from django.urls import re_path as url

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('product', ProductViewSet)



urlpatterns = [
    path('', include(router.urls)),
    url('docs/', schema_view),
]






    # path('docs/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url':'openapi-schema'}
    # ), name='swagger-ui'),
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_view':'openapi-schema'}
    # ), name='swagger-ui'),
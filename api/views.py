from django.shortcuts import render
from .serializers import UserSerializer, ProductSerializer
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from product.models import Product
from rest_framework_swagger.views import get_swagger_view
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

schema_view = get_swagger_view(title='Products API')

# from functools import wraps
# from django.http import HttpResponseRedirect

# def authors_only(function):
#   @wraps(function)
#   def wrap(request, *args, **kwargs):

#         profile = request.user.get_profile()
#         if profile.usertype == 'Author':
#              return function(request, *args, **kwargs)
#         else:
#             return HttpResponseRedirect('/')

#   return wrap

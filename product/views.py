from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.serializers import serialize

from django.http import HttpResponse

# Create your views here.

#@api_view(('GET',))
def getProduct(request):
   list = Product.objects.all()
   data = serialize("json", list)
   return HttpResponse(data, content_type="application/json")
   


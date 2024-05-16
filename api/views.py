from django.shortcuts import render
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
import json

@api_view(["GET","POST"])
def home(req,*args,**kwargs):
    serializer=ProductSerializer(data=req.data)
    if serializer.is_valid(raise_exception=True):
        return Response(serializer.data)
    return Response({"message":"invalide data"})
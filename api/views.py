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
    instance=Product.objects.all().order_by("?").first()
    print(instance)
    data={}
    data=ProductSerializer(instance).data
    # data=model_to_dict(temp,fields=['id','title','content','price','sale'])
    # data['params']=req.GET
    # data['title']=temp.title
    # data['content'] = temp.content
    # data['price'] = temp.price
    return Response({"message":["hai there",data]})

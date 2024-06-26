from rest_framework import serializers
from .models import *

class ProductSerializer(serializers.ModelSerializer):
    my_discount=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product
        fields=['title','content','price','sale','my_discount']

    def get_my_discount(self,obj):
            # if not hasattr(obj, 'id'):
            #     return None
            # if not isinstance(obj, Product):
            #     return None
            try:
                return obj.discount()
            except:
                return None

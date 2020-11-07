from rest_framework import serializers
from .models import Customer

class Customerserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('name','bill','mob_no','adress') 
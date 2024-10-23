from rest_framework import serializers
from .models import Company,CompanyBank,Medicine

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Company
        fields="__all__"
        
        
class MedicinSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicine
        fields="__all__"
        
        
class CompanyBankSerialzier(serializers.ModelSerializer):
    class Meta:
        model=CompanyBank
        fields="__all__"
        
    
    def to_representation(self, instance):
        response=super().to_representation(instance)
        response['company']=CompanySerializer(instance.company_id).data
        return response
        
    
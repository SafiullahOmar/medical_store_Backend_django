from django.shortcuts import render
from rest_framework import viewsets
from .models import Company
from .serializers import CompanySerializer
from rest_framework.response     import Response 
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class CompanyViewSet(viewsets.ViewSet):
    # queryset=Company.objects.all()
    # serializer_class=CompanySerializer
    
    
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    
    
    def list(self, request, *args, **kwargs):
        company=Company.objects.all()
        serializer=CompanySerializer(company,many=True,context={"request":request})
        response_dict={"error":False,"message":"All Company List Data","data":serializer.data}
        return Response(response_dict)
    
    def create(self,request):
        try:
            serializer=CompanySerializer(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            response_dict={"error":False,"message":"saved successfully "}
        except:
            response_dict={"error":True,"message":"Error while saving data"}
        
        return Response(response_dict)
    
    def update(self,request,pk=None):
        try:
            queryset=Company.objects.all()
            compan=get_object_or_404(queryset,pk=pk)
            serializer=CompanySerializer(compan,data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            response_dict={"error":False,"message":"updated successfully "}
        except Exception as e:
            response_dict={"error":True,"message":"Errro in updating the data ","exception erro":e}
        
        return Response(response_dict)
            
        

company_list=CompanyViewSet.as_view({"get":"list"})
company_create=CompanyViewSet.as_view({"post":"create"})
company_update=CompanyViewSet.as_view({"put":"update"})

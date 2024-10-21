from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,CompanyBank
from .serializers import CompanySerializer,CompanyBankSerialzier
from rest_framework.response     import Response 
from rest_framework.generics import get_object_or_404,ListAPIView
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
            
       
       
class CompanyBankViewSet(viewsets.ViewSet):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
     
     
    def list(self,request):
        companBank=companBank.objects.all()
        serializer=CompanyBankSerialzier(companBank,many=True,context={"request":request})
        
        response_dict={"error":False,"message":"All Company Bank List Data","data":serializer.data}
        return Response(response_dict)
    
    def create(self,request):
        try:
            
            serializer=CompanyBankSerialzier(data=request.data,context={"request":request})
            serializer.is_valid()
            serializer.save()
            response_dict={"error":False,"message":"saved successfully into cmopany Bank "}
        except:
            
            response_dict={"error":True,"message":"Error while saving data"}
        return Response(response_dict)
    
    def retrieve(self,request,pk=None):
        try:
            queryset=CompanyBank.objects.all()
            companBank=get_object_or_404(queryset,pk=pk)
            serializer=CompanyBankSerialzier(companBank,context={"request":request})
            return Response({"eror":None,"message":"signle data","data":serializer.data})
        except:
            response_dict={"error":True,"message":"Error while retriving data"}
            return Response(response_dict)
            
    def update(sef,request,pk=None):
        try:
            queryset=CompanyBank.objects.all()
            companBank=get_object_or_404(queryset,pk=pk)
            serializer=CompanyBankSerialzier(companBank,data=request.data,context={"request":request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response_dict={"error":False,"message":"updated successfully "}
        except:
            response_dict={"error":True,"message":"some error occured  "}
        
        return Response(response_dict)
            
        
        
class CompanyNameViewset(ListAPIView):
    serializer_class=CompanySerializer
    def get_queryset(self):
        name=self.kwargs["name"]
        return Company.objects.filter(name=name)
         

company_list=CompanyViewSet.as_view({"get":"list"})
company_create=CompanyViewSet.as_view({"post":"create"})
company_update=CompanyViewSet.as_view({"put":"update"})

from django.shortcuts import render

# Create your views here.
from app.models import *
from rest_framework .decorators import APIView
from app.serializers import *
from rest_framework.response import Response

class ProductData(APIView):
    def get(self,request,Pid):
        PD=Product.objects.all()
        JD=ProductModelSerializers(PD,many=True)
        # PD=Product.objects.get(Pid=Pid)
        # JD=ProductModelSerializers(PD)
        return Response(JD.data)
    

    def post(self,request,Pid):
        JD=request.data
        PD=ProductModelSerializers(data=JD)
        if PD.is_valid():
            PD.save()
            return Response({"message":'Data Inserted Successfully'})
        else:
            return Response({"message":"Data is Not Inserted"})
        
    def put(self,request,Pid):
        CJD=request.data
        PO=Product.objects.get(Pid=CJD['Pid'])
        PD=ProductModelSerializers(PO,data=CJD)
        if PD.is_valid():
            PD.save()
            return Response({"message":'Data Updated Successfully'})
        else:
            return Response({"message":"Data is Not Updated"})

    def patch(self,request,Pid):
        CJD=request.data
        PO=Product.objects.get(Pid=CJD['Pid'])
        PD=ProductModelSerializers(PO,data=CJD,partial=True)
        if PD.is_valid():
            PD.save()
            return Response({"message":'Data Updated Successfully'})
        else:
            return Response({"message":"Data is Not Updated"})

    def delete(self,request,Pid):
        PD=Product.objects.get(Pid=Pid)
        PD.delete()
        return Response({"message":"Deleted Successfully"})

   
        
    
     
            
        
        
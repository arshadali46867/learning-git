from django.shortcuts import render 
from django.http import HttpResponse
from django.views import View
from app.saveData import SaveData
from rest_framework.viewsets import ViewSet

# Create your views here.



class Student(ViewSet):
    def post(self,request):
        print(type(request))
        print(request)
        obj = SaveData()
        obj.saveDataToDb(request)
        return HttpResponse('Data Saved')   
        
    


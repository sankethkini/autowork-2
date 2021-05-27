# from django.shortcuts import render
import pickle
from django.contrib.sessions.models import Session
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings              
from django_rest_params.decorators import params
import numpy
import dill
import lime
import lime.lime_tabular


@api_view(["GET"])
def Predict(request):
    try:  
       loc=int(request.query_params['loc'])
       yr=int(request.query_params['yr'])
       kd=int(request.query_params['kd'])
       ft=int(request.query_params['ft'])
       tr=int(request.query_params['tr'])
       ot=int(request.query_params['ot'])
       ml=float(request.query_params['ml'])
       eng=int(request.query_params['eng'])
       po=float(request.query_params['po'])
       st=float(request.query_params['st'])
       np=float(request.query_params['np'])
       md=int(request.query_params['md'])
       ds={'Fuel_Type':{1:'petrol',2:'diesel',3:'LPG'},
       'Location':{0:'Ahamadabad',1:'Bengaluru',2:'Chennai',3:'Coimbatore',4:'Delhi',5:'Jaipur',6:'Kochi',7:'Kolkata',8:'Mumbai',9:'Pune'},
       'Owner_Type':{1:'first',2:'second',3:'third',4:'fourth and above'},
       'Transmission':{1:'Manual',2:'Automatic'}}
       pars=[loc,yr,kd,ft,tr,ot,ml,eng,po,st,np,md]
       inp=numpy.array(pars).reshape(1,-1)
       if np<8:
           model=pickle.load(open('./models/hyundail.pickel','rb'))
           res=model.predict(inp)
           res=float(res[0])
           inp=inp[0]
           with open('./lime/hyundaillime', 'rb') as f:
                k=dill.load(f)
           data = k.explain_instance(inp, model.predict, num_features=12)
           data1=dict(data.as_list())
           keys=list(data1)
           vals=list(data1.values())
           resl={}
           for i in range(len(keys)):
                arr=keys[i].split(' ')
                found=False
                for j in arr:
                    if j in ds.keys():
                        resl[j+' '+ds[j][1]]=vals[i]
                        found=True
                if not found:
                    resl[keys[i]]=vals[i]      
           resl['res']=round(res,2)
           print(resl)
           return JsonResponse({"result":resl})
       elif np>=8:
           model=pickle.load(open('./models/hyundaih.pickel','rb'))
           res=model.predict(inp)
           res=float(res[0])
           print(res)
           inp=inp[0]
           with open('./lime/hyundaihlime', 'rb') as f:
                k=dill.load(f)
           data = k.explain_instance(inp, model.predict, num_features=12)
           data1=dict(data.as_list())
           keys=list(data1)
           vals=list(data1.values())
           resl={}
           for i in range(len(keys)):
                arr=keys[i].split(' ')
                found=False
                for j in arr:
                    if j in ds.keys():
                        resl[j+' '+ds[j][1]]=vals[i]
                        found=True
                if not found:
                    resl[keys[i]]=vals[i]      
           resl['res']=round(res,2)
           print(resl)
           return JsonResponse({"result":resl})   
       else:
           return Response('abcd',status.HTTP_400_BAD_REQUEST)     
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)



# from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
from django_rest_params.decorators import params
import numpy
import xgboost as xgb
import dill
import lime
import lime.lime_tabular
model=xgb.XGBRegressor()
model1=xgb.XGBRegressor()

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
       ft1={1:'petrol',2:'diesel',3:'LPG'}
       loc1={0:'Ahamadabad',1:'Bengaluru',2:'Chennai',3:'Coimbatore',4:'Delhi',5:'Jaipur',6:'Kochi',7:'Kolkata',8:'Mumbai',9:'Pune'}
       ot1={0:'first',1:'second',3:'third',4:'fourth and above'}
       tr1={1:'Manual',2:'Automatic'}
       pars=[loc,yr,kd,ft,tr,ot,ml,eng,po,st,np,md]
       inp=numpy.array(pars).reshape(1,-1)
       if np<8:
           model.load_model('./models/hyundail.json')
           res=model.predict(inp)
           res=float(res[0])
           print("this one")
           print(loc1[loc])
           inp=inp[0]
           with open('./lime/hyundail', 'rb') as f:
                k=dill.load(f)
           data = k.explain_instance(inp, model.predict, num_features=12)
           data1=dict(data.as_list())
           keys=list(data1)
           values=list(data1.values())
           keys[2]='Transmission '+tr1[tr]
           keys[3]='Location '+loc1[loc]
           keys[4]='Owner '+ot1[ot]
           keys[6]='Fuel '+ft1[ft]
           data1={}
           for i in range(len(keys)):
               data1[keys[i]]=values[i]
           data1['res']=round(res,2)
           print(data1)
           return JsonResponse({"result":data1})
       elif np>=8:
           model.load_model('./models/hyundaih.json')
           res=model.predict(inp)
           res=float(res[0])
           inp=inp[0]
           print("this one 1")
           with open('./lime/hyundaih', 'rb') as f:
                k=dill.load(f)
           data = k.explain_instance(inp, model.predict, num_features=12)
           data1=dict(data.as_list())
           keys=list(data1)
           values=list(data1.values())
           keys[2]='Transmission '+tr1[tr]
           keys[3]='Location '+loc1[loc]
           keys[4]='Owner '+ot1[ot]
           keys[6]='Fuel '+ft1[ft]
           data1={}
           for i in range(len(keys)):
               data1[keys[i]]=values[i]
           data1['res']=round(res,2)
           print(data1)
           return JsonResponse({"result":data1})
       else:
           return Response('abcd',status.HTTP_400_BAD_REQUEST)     
    except ValueError as e:
        return Response(e.args[0],status.HTTP_400_BAD_REQUEST)



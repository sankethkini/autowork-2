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
from django_rest_params.decorators import params
import numpy
import pickle
import dill
import lime
import lime.lime_tabular
from django.shortcuts import render,redirect
from django.conf import settings
from allauth.account.models import EmailAddress
from django.core.mail import send_mail
from .forms import Email

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
           model=pickle.load(open('./models/marutil.pickel','rb'))
           res=model.predict(inp)
           res=float(res[0])
           inp=inp[0]
           with open('./lime/marutillime', 'rb') as f:
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
           model=pickle.load(open('./models/marutih.pickel','rb'))
           res=model.predict(inp)
           res=float(res[0])
           inp=inp[0]
           with open('./lime/marutihlime', 'rb') as f:
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


def login(request):
    if request.user.is_authenticated:
        return redirect('http://localhost:3000')
    else:
        return render(request,'maruti/signin.html')

def send_email(request):
    if request.POST:
        if request.user.is_superuser:
            try:
                form=request.POST
                subject = form['subject']
                message = form['message']
                print(subject,message)
                email_from = settings.EMAIL_HOST_USER
                alladress=[]
                emails=EmailAddress.objects.all()
                for i in emails:
                    alladress.append(i.email)
                recipient_list=alladress
                send_mail( subject, message, email_from, recipient_list )
                return HttpResponse('<h1>Sent Successfuly</h1>')
            except:
                return HttpResponse('<h2>error occured<h2>')
        else:
            return HttpResponse('<h1>Permission Denied<h1>')

    else:
        form=Email()
        return render(request,'maruti/send_email.html',{'forms':form})

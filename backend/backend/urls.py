
from django.contrib import admin
from django.urls import path,re_path,include
from django.views.generic import TemplateView
from hyundai import views as vh
from maruti import views as vm
from maruti import templates

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',vm.login),
    path('send_email/',vm.send_email),
    re_path(r'^apih/',vh.Predict),
    re_path(r'^apim/',vm.Predict),
    path('accounts/', include('allauth.urls')),
]

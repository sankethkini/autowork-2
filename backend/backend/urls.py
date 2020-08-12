
from django.contrib import admin
from django.urls import path,re_path
from django.views.generic import TemplateView
from hyundai import views as vh
from maruti import views as vm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name='index.html')),
    re_path(r'^apih/',vh.Predict),
    re_path(r'^apim/',vm.Predict)
]

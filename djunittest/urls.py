
from django.contrib import admin
from django.urls import path
from appone.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomePageView.as_view(),name = "home"),
    path('login/', LoginPageView.as_view(),name = 'login'),
    path('emps/', EmpsPageView.as_view(),name = 'emplist'),
]


#PYTHON --> URI1,2,3

#%PYTHON_HOME%\
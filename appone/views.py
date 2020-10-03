from django.shortcuts import render
from django.views.generic import TemplateView,ListView  # consumer -> client side in build functionality -->Enduser--> Consumer Side
from appone.models import *

#modular -->

class HomePageView(TemplateView): #generic
    template_name = 'home.html'

class LoginPageView(TemplateView):
    template_name = 'login.html'

#--> end user --> Ui --> not services --> django --> Listview/Createview/UpdateView/DeleteView
class EmpsPageView(ListView): # --> object_list --> already in response -->only to show case list of data-->fetchall
    model = Employee
    template_name = 'emp.html'


'''
class AddressPageView(ListView):
    model = Address
    template_name = 'address.html'

from rest_framework.viewsets import ModelViewSet #api -- > api --> server side la--> producer
class EmpViewSet(ModelViewSet):     # end user services--> not -->ui --> 6 apis--> code ? --no
    queryset = Employee.query.all()
    serializer_class = None
def abcd(req):
    return render(req,'emp.html',{"emps" : None,"address" :None,"XYZ" : None})
'''
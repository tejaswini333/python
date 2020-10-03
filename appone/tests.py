from django.test import TestCase,SimpleTestCase
from django.urls import reverse
from appone.models import Employee
from appone.empservice import EmpServiceOp

service = EmpServiceOp()
#client --> TestCase--> SimpleTest --> read --.>

#selenium data enter -- Automation --> api --> functionality testing --

#pytest/unitest -->


class EmpPageTest(TestCase):

    def setUp(self):
        pass

    def tearDown(self) :
        pass

    def test_create_emp_success(self):
        emp1 = Employee.objects.create(id=103,name='XXXXX',age=44,salary=3993.45,address='Solapur') #save
        emp2 = Employee.query.filter(id=103).first() #get -->
        self.assertEqual(emp1.name,emp2.name)
        self.assertEqual(emp1.age, emp2.age)
        self.assertEqual(emp1.salary, emp2.salary)
        self.assertEqual(emp1.address, emp2.address)


    def test_create_emp(self):
        emp = Employee.objects.all()[-1]  #1-10 [-1]----> 10
        #intput --{"name":"XXX","salary":3333.34,"age":23,"address":"Pune"}
        output = service.add_new_emp({"name":"XXX","salary":3333.34,"age":23,"address":"Pune"}) #11
        self.assertEqual(output,emp.id+1) #11  --> 10+1
        femp = Employee.objects.get(output)
        #femp --> same

    def test_one_emp_one_address(self):
        pass

    def test_one_emp_with_noaddress(self):
        pass  #srs

    def test_one_emp_with_many_address(self):
        pass

    def test_fetch_emp_check_list_address(self):
        pass

    def test_fetch_address_thru_emp(self):
        pass





class TestHomePage(SimpleTestCase):

    def test_home_working_or_not(self): # client --> ui --> dynamic url
        response = self.client.get('/home/')
        print(response.status_code) #200
        self.assertEqual(response.status_code,200,'Link is broken--> home page url is not working')

    def test_home_page_by_constant_url(self):   # fixed -->
        response = self.client.get(reverse('home'))
        print(response.status_code)  # 200
        self.assertEqual(response.status_code, 200, 'Link is broken--> home page url is not working')

    def test_home_page_correct_template(self):
        response = self.client.get(reverse('home'))
        print(response)
        self.assertTemplateUsed(response,'home.html')
        self.assertTemplateNotUsed(response, 'login.html')

    def test_home_page_contents(self):
        response = self.client.get('/home/')
        print(response)
        self.assertContains(response,'101,Yogesh...')

    def test_home_page_contents(self):

        response = self.client.get('/emp/')  #url --> hit
        emps = Employee.query.all()  # 5 -->
        self.assertEqual(len(emps),5)# 5
        print(response) # response ==> msg -->      !No records-->
        self.assertNotContains(response,'No Records') # ! no records-->loop fail ?  #no records
        # 5 --> show  ?
        # response.context-->? ??
        #response.text --> <tr> --> 5

'''
class TestLoginPage(SimpleTestCase):

    def test_login_working_or_not(self):
        pass

    def test_login_page_by_constant_url(self):
        pass

    def test_login_page_correct_template(self):
        pass

    def test_login_page_contents(self):
        pass
'''
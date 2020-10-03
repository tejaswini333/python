from appone.models import Employee

class EmpServiceOp:

    def add_new_emp(self,emp):
        emp = Employee(salary=emp['salary'],
                                name=emp['name'],
                                age=emp['age'],
                                address=emp['address'])
        emp.save()
        return emp.id


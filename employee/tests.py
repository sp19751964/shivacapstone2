from django.test import TestCase
from employee.models import Employee

from django.core.files import File

class EmployeeTestCase(TestCase):
	def setUp(self):
		Employee.objects.create(id=22, ename="Employee22", eemail="Employee22@email.com", econtact=123456789 )

	def test_employee_retrieve(self):
		obj = Employee.objects.get(id=22)
		self.assertEqual(obj.ename, "Employee22")

	def test_employee_update(self):
		obj = Employee.objects.get(id=22)
		obj.ename = "Employee22UpdatedFromTestcases"
		obj.save()
		print("\nObject updated!")
		newObj = Employee.objects.get(id=22)
		self.assertEqual(newObj.ename, 'Employee22UpdatedFromTestcases')

	def test_employee_delete(self):
		count = Employee.objects.count()
		obj = Employee.objects.get(id=22)
		obj.delete()
		newCount = Employee.objects.count()
		print(count, newCount)
		self.assertEqual(count-1, newCount)

from django.test import TestCase
from .models import Employee


class TestEmployee(TestCase):
    def setUp(self) -> None:
        Employee.objects.create(
            first_name="Hediberto",
            last_name="C. Silva",
            pis=12071377038,
            actived=True)

    def test_employees_is_actived(self) -> None:
        employee = Employee.objects.get(pis=12071377038)
        self.assertEqual(employee.is_actived(), True)
        
    def test_employees_is_valid(self) -> None:
        employee = Employee.objects.get(pis=12071377038)
        self.assertEqual(employee.is_valid(), True)

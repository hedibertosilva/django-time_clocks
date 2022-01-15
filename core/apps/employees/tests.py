from django.test import TestCase
from .models import Employee


class TestEmployee(TestCase):
    def setUp(self) -> None:
        Employee.objects.create(
            first_name="Hediberto",
            last_name="C. Silva",
            pis=63652448133,
            actived=True)

    def test_employees_is_actived(self) -> None:
        employee = Employee.objects.get(pis=63652448133)
        self.assertEqual(employee.is_actived(), True)
        
    def test_employees_is_valid_pis(self) -> None:
        employee = Employee.objects.get(pis=63652448133)
        self.assertEqual(employee.is_valid_pis(), True)

from math import remainder
from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=155, null=True, blank=True)
    pis = models.PositiveIntegerField()
    actived = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "%s %s" % (self.first_name, self.last_name)

    def is_actived(self):
        return self.actived == True

    def is_valid_pis(self):
        pis = f'{self.pis:011}'
        digit = int(pis[-1])
        weights = (3, 2, 9, 8, 7, 6, 5, 4, 3, 2)

        remainder = sum(int(n) * w for n, w in zip(pis, weights))%11
        remainder = 11 - remainder
        
        if remainder in (10, 11):
            return True if digit == 0 else False
        if remainder != digit:
            return False
        return True

    class Meta:
        default_related_name = "employee"
        verbose_name = "employee"
        verbose_name_plural = "employees"
        constraints = [
            models.UniqueConstraint(
                name="unq_pis",
                fields=['pis']),
            models.UniqueConstraint(
                name="unq_fist_and_last_name",
                fields=['first_name', 'last_name'])]
        
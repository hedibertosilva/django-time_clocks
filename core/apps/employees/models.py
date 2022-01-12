from django.db import models


class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=155, null=True, blank=True)
    pis = models.PositiveIntegerField()
    actived = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "{} {}" % (self.first_name, self.last_name)

    def is_actived(self):
        return self.actived == True

    def is_valid(self):
        return len(str(self.pis)) == 11

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
        
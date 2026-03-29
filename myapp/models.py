from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)   # ✅ prevent duplicate emails
    age = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)  # ✅ for "New Employees"

    def __str__(self):
        return self.name
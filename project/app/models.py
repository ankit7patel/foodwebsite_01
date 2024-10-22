from django.db import models

# Create your models here.
class student(models.Model):
    stu_name = models.CharField(max_length=50)
    stu_email = models.EmailField()
    stu_contact = models.IntegerField()
    stu_password = models.CharField(max_length=50)
    stu_confirm_password = models.CharField(max_length=128)

    def __str__(self):
        return self.stu_name
    

class Query(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    query=models.TextField()

    def __str__(self):
        return self.query
    


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    count = models.PositiveIntegerField()
    food_name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.food_name}"
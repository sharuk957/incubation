from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Incubation(models.Model):
    Name = models.CharField(max_length=250)
    Address = models.CharField(max_length=1000)
    City = models.CharField(max_length=250)
    State = models.CharField(max_length=250)
    Email = models.EmailField()
    Phone = models.CharField(max_length=250)
    Company_Name = models.CharField(max_length=250)
    Company_Logo = models.ImageField(upload_to='pics')
    Team_Description = models.TextField(max_length=2500)
    Company_Description = models.TextField(max_length=2500)
    Problem_Description = models.TextField(max_length=2500)
    Solution_Description = models.TextField(max_length=2500)
    Proposition_Description = models.TextField(max_length=2500)
    Competitors_Description = models.TextField(max_length=2500)
    Revenue_Model = models.TextField(max_length=2500)
    Potential_Market_Size = models.TextField(max_length=2500)
    Team_Description = models.TextField(max_length=2500)
    Marketting_Plan = models.TextField(max_length=2500)
    Incubation_Type = models.CharField(max_length=100)
    Business_Proposal = models.TextField(max_length=2500)
    Status = models.CharField(max_length=250)
    def __str__(self):
        return self.Name + ", " + self.Company_Name
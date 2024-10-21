from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)  

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=200)  
    company = models.CharField(max_length=100) 
    description = models.TextField()  
    location = models.CharField(max_length=100)  
    salary = models.DecimalField(max_digits=10, decimal_places=2)  
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)  
    date_posted = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return self.title



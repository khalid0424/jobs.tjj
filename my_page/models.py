from django.db import models



class User_profie(models.Model):
    name = models.CharField(max_length=25)
    surename = models.CharField(max_length=25)
    date_birth =models.DateTimeField()
    phone_number = models.CharField(max_length=12)
    emai = models.EmailField(max_length=25)
    password = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='images/', blank=True)
    role = models.CharField(max_length=50, choices=[
    ('worker', 'Коргар'),
    ('korfarmo', 'Корфармо'),
    ('none', 'ҳеҷ'),]) 


    def __str__(self):
        return f"{self.name} {self.surename}"
  

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
    image_poster= models.ImageField(upload_to='images/', blank=True)
    

    def __str__(self):
      return self.title



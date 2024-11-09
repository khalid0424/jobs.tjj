
from django.contrib import admin
from .models import Job, Category 



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')  
    search_fields = ('name',)  

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'company', 'location', 'salary', 'category', 'date_posted')
    search_fields = ('title', 'company', 'location') 
    list_filter = ('category', 'location', 'date_posted')






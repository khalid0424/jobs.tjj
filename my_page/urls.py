from django.urls import path, include
from .views import home,create_job,job_detail


urlpatterns = [
    path('', home, name='home'),
    path('job/<int:job_id>/', job_detail, name='job_detail'),
    path('job/create/', create_job, name='job_create'),

]
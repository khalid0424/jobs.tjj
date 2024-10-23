from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Job, Category,User_profie




def home(request):
    query = request.GET.get('q', '') 
    category_filter = request.GET.get('category', None) 
    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)  

    if category_filter:
        jobs = jobs.filter(category__id=category_filter)  

    categories = Category.objects.all()  

    context = {
        'jobs': jobs,
        'categories': categories,

    }

    return render(request, 'home.html', context)

def create_job(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company')
        description = request.POST.get('description')
        location= request.POST.get('location')
        salery = request.POST.get('salery')
        category = request.POST.get('category')
        date_post= request.POST.get(' date_post')
        image_poster = request.POST.get('image_poster')


        job = Job(title=title,company=company, description=description,location=location,salery=salery,date_post=date_post,category=category, image_poster=image_poster, posted_by=request.user)
        job.save()
        return redirect('home')
    
    create = Category.objects.all()
    return render(request,'job.html',{'create':create})



def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id) 
    return render(request, 'job_detail.html', {'job': job})



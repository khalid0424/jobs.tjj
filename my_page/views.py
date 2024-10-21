from django.shortcuts import render
from .models import Job, Category

# Намоиши рӯйхати корҳо
def home(request):
    query = request.GET.get('q', '')  # Барои ҷустуҷӯи кор бо номи ширкат ё кор
    category_filter = request.GET.get('category', None)  # Филтр барои соҳа
    jobs = Job.objects.all()

    if query:
        jobs = jobs.filter(title__icontains=query)  # Ҷустуҷӯ бо унвон

    if category_filter:
        jobs = jobs.filter(category__id=category_filter)  # Филтр бо категория

    categories = Category.objects.all()  # Ҳама категорияҳо барои филтр

    context = {
        'jobs': jobs,
        'categories': categories,
    }

    return render(request, 'templates/home.html', context)

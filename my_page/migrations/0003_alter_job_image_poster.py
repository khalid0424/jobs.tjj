# Generated by Django 5.0 on 2024-10-31 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_page', '0002_job_image_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image_poster',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
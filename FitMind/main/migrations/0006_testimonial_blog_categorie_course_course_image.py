# Generated by Django 4.1.2 on 2024-05-04 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_course_bundle'),
    ]

    operations = [
        migrations.CreateModel(
            name='testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='D:\\Reallife\\FitMind2.0\\FitMind\\static\\media\testimonial\testimonial-1.jpg', upload_to='static/media/test')),
                ('text', models.TextField()),
                ('name', models.CharField(max_length=255)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='categorie',
            field=models.CharField(default='defualt', max_length=200),
        ),
        migrations.AddField(
            model_name='course',
            name='course_image',
            field=models.ImageField(default='D:\\Reallife\\FitMind2.0\\FitMind\\static\\media\testimonial\testimonial-1.jpg', upload_to='static/media/course'),
        ),
    ]

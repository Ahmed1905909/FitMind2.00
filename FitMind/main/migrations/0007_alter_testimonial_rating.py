# Generated by Django 4.1.2 on 2024-05-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_testimonial_blog_categorie_course_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='rating',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]

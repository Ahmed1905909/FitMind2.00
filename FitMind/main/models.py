from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField

class Blog(models.Model):
    image = models.ImageField(upload_to='static/media/blog')
    title = models.CharField(max_length=200)
    categorie = models.CharField(max_length=200,  default='defualt')
    by_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now_add=True)
    about = models.CharField(max_length=200, default='About this blog') 
    content = RichTextField()

    def __str__(self):
        return self.title
    
class Course(models.Model):
    course_image = models.ImageField(upload_to='static/media/course',  default='D:\Reallife\FitMind2.0\FitMind\static\media\testimonial\testimonial-1.jpg')
    course_name = models.CharField(max_length=255)
    course_price = models.DecimalField(max_digits=6, decimal_places=2)
    course_description = models.TextField()

    def __str__(self):
        return self.course_name
    

class Bundle(models.Model):
    name = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course)
    bundle_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
    
class testimonial(models.Model):
    img = models.ImageField(upload_to='static/media/test',  default='D:\Reallife\FitMind2.0\FitMind\static\media\testimonial\testimonial-1.jpg')
    text = models.TextField()
    name= models.CharField(max_length=255)
    rating =  models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
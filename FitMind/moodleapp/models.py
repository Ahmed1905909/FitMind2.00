from django.db import models
from ckeditor.fields import RichTextField
from main.models import Course  # Ensure this import is correct
# Create your models here.
class CourseContent(models.Model):
    page_id = models.AutoField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    page_number = models.IntegerField()
    title = models.CharField(max_length=255)
    content = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    # page_weight = models.IntegerField()



class Document(models.Model):
    title = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='documents/')

from django import forms
from .models import Blog , Course , testimonial
from ckeditor.widgets import CKEditorWidget

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['image', 'title', 'categorie','about','content']
        widgets = {
            'content': CKEditorWidget(),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_image','course_name', 'course_price', 'course_description']

class testimonialForm(forms.ModelForm):
    class Meta:
        model = testimonial
        fields = ['img' , 'text','name' , 'rating']
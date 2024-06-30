from django import forms
from .models import CourseContent , Document
from ckeditor.widgets import CKEditorWidget

class CourseContentForm(forms.ModelForm):
    class Meta:
        model = CourseContent
        fields = ['course', 'page_number', 'title', 'content', ]
        widgets = {
            'content': CKEditorWidget(),
        }




class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'file',)

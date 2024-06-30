from django.shortcuts import render, redirect , get_object_or_404
from .forms import CourseContentForm , DocumentForm
from .models import CourseContent , Document
from main.models import Course
from docx import Document as DocxDocument
from django.core.paginator import Paginator
import mammoth
import aspose.words as aw
from django.views.decorators.clickjacking import xframe_options_exempt


# Create your views here.
def moodleindex(request):
    return render(request, 'moodleindex.html')



def add_course_content(request):
    if request.method == 'POST':
        form = CourseContentForm(request.POST)
        if form.is_valid():
            form.save()
            if 'save_add_another' in request.POST:
                return redirect('createcourse') 
            else:
                return redirect('moodleindex')
    else:
        form = CourseContentForm()
    return render(request, 'create_course.html', {'form': form})


def view_course_content(request, course_id, page_number=1):
    try:
        content = CourseContent.objects.filter(course_id=course_id, page_number=page_number).first()
        total_pages = CourseContent.objects.filter(course_id=course_id).count()
    except CourseContent.DoesNotExist:
        content = None
        total_pages = 0

    context = {
        'content': content,
        'total_pages': total_pages,
        'current_page': page_number,
        'course_id': course_id
    }
    return render(request, 'view_course_content.html', context)



def document_list(request):
    documents = Document.objects.all()
    return render(request, 'document_list.html', {'documents': documents})

import aspose.words as aw

def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form first to get the file saved
            document = form.save()
            # Convert the document to HTML and save the HTML content
            doc = aw.Document(document.file.path)
            html_output = document.file.path + ".html"
            doc.save(html_output, aw.SaveFormat.HTML)
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'upload_document.html', {'form': form})


def view_document(request, pk):
    document = get_object_or_404(Document, pk=pk)
    html_file_path = document.file.path + ".html"
    with open(html_file_path, "r") as file:
        html_content = file.read()

    return render(request, 'view_document.html', {'document': document, 'html_content': html_content})


def listtest(request, course_id=1 , page_number=1):
    context = {
                'current_page': page_number,
        'course_id': course_id
    }
    return render(request, 'listtry.html',context)
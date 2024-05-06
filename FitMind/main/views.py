from django.shortcuts import render, redirect , get_object_or_404
from .forms import BlogForm , CourseForm
from .models import Blog , Course , Bundle , testimonial
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    courses = Course.objects.all()
    testimonials = testimonial.objects.all()
    context = {'courses': courses, 'testimonials': testimonials}
    return render(request, 'index.html', context)


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})


def testblog(request):
    blogs = Blog.objects.all()
    return render(request, 'testblog.html', {'blogs': blogs})




def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blog_detail.html', {'blog': blog})

@login_required
def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.by_user = request.user
            blog.save()
            return redirect('blog')
    else:
        form = BlogForm()
    return render(request, 'add_blog.html', {'form': form})


def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def create_bundle(request):
    if request.method == 'POST':
        bundle_name = request.POST.get('bundle_name')
        bundle_price = request.POST.get('bundle_price')
        bundle = Bundle.objects.create(name=bundle_name, bundle_price=bundle_price)
        bundle.courses.set(courses)
        bundle.save()
        return redirect('index')
    else:
        courses = Course.objects.all()
        return render(request, 'add_course.html', {'course': courses})
    

def custom_404(request, exception):
       return render(request, '404.html', {}, status=404)
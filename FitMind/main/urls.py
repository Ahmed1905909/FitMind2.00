from django.urls import path
from main import views

urlpatterns = [
path('', views.index, name='index'),
path('Blog/', views.blog, name='blog'),
path('AddBlog/', views.addblog, name='addblog'),
path('test/', views.testblog, name='testblog'),
path('blogs/<int:blog_id>/', views.blog_detail, name='blog-detail'),
path('addcourse/', views.create_course, name='add-course'),
path('addbundle/', views.create_bundle, name='add-bundle'),

]
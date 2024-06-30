from django.urls import path
from moodleapp import views

urlpatterns = [
    path('', views.moodleindex, name='moodleindex'),
    path('createcourse/', views.add_course_content, name='createcourse'),
    path('course/<int:course_id>/page/<int:page_number>/', views.view_course_content, name='view_course_content'),
    path('upload/', views.upload_document, name='upload_document'),
    path('list', views.document_list, name='document_list'),
    path('listtest', views.listtest, name='listtest'),
    path('view/<int:pk>/', views.view_document, name='view_document'),


]
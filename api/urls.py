from django.urls import path,include
from . import  views
urlpatterns=[
    path('', views.student_detail),
    path('create',views.student_create),
    path('studentapi',views.student_api)
]
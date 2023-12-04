from django.urls import path
from . import views
urlpatterns=[
    path('', views.hello_word),
    path('teach_api/<int:pk>',views.tech_api),
    path('techerView',views.teacherView.as_view()),
    path('tech_detail/<int:pk>',views.TechDetail.as_view()),
    path('tech_list',views.TechList.as_view()),
    path('teach_list2',views.List.as_view())

]
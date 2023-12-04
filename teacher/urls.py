from django.urls import path
from . import views
urlpatterns=[
    path('', views.hello_word),
    path('teach_api/<int:pk>',views.tech_api)

]
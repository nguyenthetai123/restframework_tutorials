from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('post',views.PostViewset,basename='postss')


urlpatterns=[
    path('', include(router.urls)),
    path('signup', views.SignupView.as_view(),name='msignup')
]
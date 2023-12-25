from django.urls import path,include

from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register('core',views.StudentView,basename='studentView')
router.register('core2',views.StudentView1,basename='studentView1')
urlpatterns=[
    path('', include(router.urls)),
]
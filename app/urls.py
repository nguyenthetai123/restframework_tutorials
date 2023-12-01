from django.urls import path,include
from . import views
urlpatterns=[
    path('employee',views.employeeListView,name='employee_list'),
    path('home', views.homepage),
    path('', views.PostListCreateView.as_view()),
    # path('lists_post',views.lists_post),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    # path('update_post/<int:id>', views.update_post),
    # path('delete/<int:id>',views.delete_post)
    path('post2/',views.PostList_two.as_view())
]
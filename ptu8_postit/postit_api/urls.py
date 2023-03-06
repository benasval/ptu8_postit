from django.urls import path
from . import views


urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('<int:post_id>/comments/', views.CommentList.as_view()),
    path('comment/<int:pk>/', views.CommentDetail.as_view()),
]

from django.urls import path
from . import views
urlpatterns = [
    path('category/', views.category_list_create),
    path('articles/', views.article_list_create),
    path('article/<int:article_pk>/', views.article_detail),
    path('article/<int:article_pk>/comments/', views.comment_create),
    path('comment/<int:comment_pk>/', views.comment_detail)
]

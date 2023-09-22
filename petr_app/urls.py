from django.urls import path
from .views import (CategoryListCreateView, CategoryDetailView, TagView,
                    TagDetailView, PostListCreateView, PostDetailView)


urlpatterns = [
    # path('categories/', category_list),
    # path('category_create/', category_create),
    # path('categories/<int:pk>/', category_detail),
    # path('categories/<int:pk>/update/', update),
    # path('categories/<int:pk>/delete/', delete),
    path('categories/', CategoryListCreateView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('tags/', TagView.as_view()),
    path('tags/<int:pk>/', TagDetailView.as_view()),
    path('posts/', PostListCreateView.as_view()),
    path('posts/<int:pk>/', PostDetailView.as_view()),
]


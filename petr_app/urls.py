from django.urls import path
from .views import category_list, category_create, category_detail, update, delete


urlpatterns = [
    path('categories/', category_list),
    path('category_create/', category_create),
    path('categories/<int:pk>/', category_detail),
    path('categories/<int:pk>/update/', update),
    path('categories/<int:pk>/delete/', delete)
]


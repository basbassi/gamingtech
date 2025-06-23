from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:category_id>/', views.category_products, name='category_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('blog/', views.blog, name='blog'),
    path('blog/article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]

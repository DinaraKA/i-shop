from django.urls import path
from webapp.views.category_views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView
from webapp.views.product_views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductListView
from webapp.views.review_views import ReviewCreateView
from webapp.views.subcategory_views import SubCategoryDeleteView, SubCategoryCreateView, SubCategoryUpdateView
from .views.orders_view import OrderListView, OrderDetailView, OrderUpdateView, OrderProductUpdateView, OrderProductDeleteView
from .views.news_views import NewsView, NewsAddView, NewsDetailView, NewsDeleteView, NewsEditView

app_name = 'webapp'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/change/<int:pk>/', CategoryUpdateView.as_view(), name='category_change'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>/subcategory_add/', SubCategoryCreateView.as_view(), name='subcategory_add'),
    path('subcategory/change/<int:pk>/', SubCategoryUpdateView.as_view(), name='subcategory_change'),
    path('subcategory/delete/<int:pk>/', SubCategoryDeleteView.as_view(), name='subcategory_delete'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order_detail"),
    path('orders/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('orders/product/update/<int:pk>/<int:id>', OrderProductUpdateView.as_view(), name='order_product_update'),
    path('orders/product/delete/<int:pk>/<int:id>', OrderProductDeleteView.as_view(), name='order_product_delete'),
    path('product_category/<int:pk>', ProductListView.as_view(), name='products_category'),
    path('review/add/<int:pk>/', ReviewCreateView.as_view(), name='review_create'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/add/', NewsAddView.as_view(), name='news_add'),
    path('news/change/<int:pk>/', NewsEditView.as_view(), name='news_edit'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
]

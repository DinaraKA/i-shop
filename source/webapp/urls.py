from django.urls import path
from webapp.views.brand_views import BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView
from webapp.views.category_views import CategoryListView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
    CategoryDetailView
from webapp.views.product_in_category_views import ProductInCategoryCreateView, ProductInCategoryListView, \
    ProductInCategoryDeleteView, ProductInCategoryUpdateView, product_in_categoryadditem, product_in_categorydeleteitem
from webapp.views.product_views import IndexView, ProductView, ProductCreateView, ProductUpdateView, ProductDeleteView, \
    ProductListView, ProductALLListView, AddToFavorites, DeleteFromFavorites, FavoritesList, SearchResultsView, \
    ProductsOfferListView, AddToOffer, DeleteFromOffer, load_subcategories, ProductListGetView, \
    ProductSubCategoryListView
from webapp.views.review_views import ReviewCreateView
from webapp.views.subcategory_views import SubCategoryDeleteView, SubCategoryCreateView, SubCategoryUpdateView
from .views.cart_views import CartView, cartdeleteitem, cartadditem, cart_modal_delete, Check
from .views.orders_view import OrderListView, OrderDetailView, OrderProductCreateView, OrderProductUpdateView, \
    OrderProductDeleteView, OrderUpdateView
from .views.news_views import NewsView, NewsAddView, NewsDetailView, NewsDeleteView, NewsEditView
from .views.delivery_cost import DeliveryCostList, DeliveryCostAdd, DeliveryView, ReturnView, DeliveryAddressAdd
from .views.carousel_views import *
from .views.compare_views import compareadditem, comparedeleteitem, CompareView, CompareChangeView
from .views.main_carousel_views import MainCarouselListView, MainCarouselCreateView, MainCarouselUpdateView, MainCarouselDeleteView
from .views.payment_views import PaymentView
from .views.color_view import *

app_name = 'webapp'


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('products/<int:pk>/', ProductView.as_view(), name='product_detail'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product_category/<int:pk>', ProductListView.as_view(), name='products_category'),
    path('product_sub_category/<int:pk>', ProductSubCategoryListView.as_view(), name='products_sub_category'),
    path('product_list/', ProductListGetView.as_view(), name='products_list_get'),
    path('product/add-to-favorites/', AddToFavorites.as_view(), name='add_to_favorites'),
    path('product/delete-from-favorites/', DeleteFromFavorites.as_view(), name='delete_from_favorites'),
    path('products_favorites/', FavoritesList.as_view(), name='favorite_products'),
    path('product/add-to-offer/', AddToOffer.as_view(), name='add_to_offer'),
    path('product/delete-from-offer/', DeleteFromOffer.as_view(), name='delete_from_offer'),
    path('products_in_offer/', ProductsOfferListView.as_view(), name='offer_products'),
    path('ajax/load-subcategories/', load_subcategories, name='ajax_load_subcategories'),
    path('categories/', CategoryListView.as_view(), name='categories_list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
    path('category/change/<int:pk>/', CategoryUpdateView.as_view(), name='category_change'),
    path('category/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    path('category/<int:pk>/subcategory_add/', SubCategoryCreateView.as_view(), name='subcategory_add'),
    path('subcategory/change/<int:pk>/', SubCategoryUpdateView.as_view(), name='subcategory_change'),
    path('subcategory/delete/<int:pk>/', SubCategoryDeleteView.as_view(), name='subcategory_delete'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name="order_detail"),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('order/product/create/<int:pk>/', OrderProductCreateView.as_view(), name='order_product_create'),
    path('order/product/update/<int:pk>/<int:id>/', OrderProductUpdateView.as_view(), name='order_product_update'),
    path('order/product/delete/<int:pk>/<int:id>/', OrderProductDeleteView.as_view(), name='order_product_delete'),
    # path('cart/change/', CartChangeView.as_view(), name='cart_change'),
    path('cart/', CartView.as_view(), name='cart'),
    path('review/add/<int:pk>/', ReviewCreateView.as_view(), name='review_create'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news_detail'),
    path('news/add/', NewsAddView.as_view(), name='news_add'),
    path('news/change/<int:pk>/', NewsEditView.as_view(), name='news_edit'),
    path('news/delete/<int:pk>/', NewsDeleteView.as_view(), name='news_delete'),
    path('brands/', BrandListView.as_view(), name='brands_list'),
    path('brand/add/', BrandCreateView.as_view(), name='brand_add'),
    path('brand/change/<int:pk>/', BrandUpdateView.as_view(), name='brand_change'),
    path('brand/delete/<int:pk>/', BrandDeleteView.as_view(), name='brand_delete'),
    path('colors/', ColorListView.as_view(), name='colors_list'),
    path('color/add/', ColorCreateView.as_view(), name='color_add'),
    path('color/change/<int:pk>/', ColorUpdateView.as_view(), name='color_change'),
    path('color/delete/<int:pk>/', ColorDeleteView.as_view(), name='color_delete'),
    path('carousel/', CarouselListView.as_view(), name='carousel_list'),
    path('carousel/add/', CarouselCreateView.as_view(), name='carousel_add'),
    path('carousel/change/<int:pk>/', CarouselUpdateView.as_view(), name='carousel_change'),
    path('carousel/delete/<int:pk>/', CarouselDeleteView.as_view(), name='carousel_delete'),
    path('carousel/change/product/<int:pk>/', CarouselAddView.as_view(), name='product_carousel_add'),
    path('carousel/products/all/', ProductALLListView.as_view(), name='products_all'),
    path('carouseldeleteitem/', carouseldeleteitem, name='carouseldeleteitem'),
    path('carouseladditem/', carouseladditem, name='carouseladditem'),
    path('cartdeleteitem/', cartdeleteitem, name='cartdeleteitem'),
    path('cartdelete/', cart_modal_delete, name='cart_modal_delete'),
    path('cartadditem/', cartadditem, name='cartadditem'),
    path('product/search/results/', SearchResultsView.as_view(), name='search_results'),
    path('deliverycost/', DeliveryCostList.as_view(), name='delivery_cost'),
    path('deliverycost/add/', DeliveryCostAdd.as_view(), name='delivery_cost_add'),
    path('delivery/', DeliveryView.as_view(), name='delivery_view'),
    path('return/', ReturnView.as_view(), name='return_view'),
    path('compareadd/', compareadditem, name='compare_add'),
    path('comparedelete/', comparedeleteitem, name='compare_delete'),
    path('compares/', CompareView.as_view(), name='compare_list'),
    path('compare/change/', CompareChangeView.as_view(), name='compare_change'),
    path('check/', Check.as_view(), name="check_cart"),
    path('main-carousel/', MainCarouselListView.as_view(), name='main_carousel_list'),
    path('main-carousel/add/', MainCarouselCreateView.as_view(), name='main_carousel_add'),
    path('main-carousel/change/<int:pk>/', MainCarouselUpdateView.as_view(), name='main_carousel_change'),
    path('maincarousel/delete/<int:pk>/', MainCarouselDeleteView.as_view(), name='main_carousel_delete'),
    path('deliveryaddress/add', DeliveryAddressAdd.as_view(), name="delivery_address_add"),
    path('payment/', PaymentView.as_view(), name='payment_view'),
    path('product_in_category/add/', ProductInCategoryCreateView.as_view(), name='product_in_category_add'),
    path('product_in_category/', ProductInCategoryListView.as_view(), name='product_in_category_list'),
    path('product_in_category/change/<int:pk>/', ProductInCategoryUpdateView.as_view(), name='product_in_category_change'),
    path('product_in_category/delete/<int:pk>/', ProductInCategoryDeleteView.as_view(), name='product_in_category_delete'),
    path('product_in_category_deleteitem/', product_in_categorydeleteitem, name='product_in_category_deleteitem'),
    path('product_in_category_additem/', product_in_categoryadditem, name='product_in_category_additem'),

]

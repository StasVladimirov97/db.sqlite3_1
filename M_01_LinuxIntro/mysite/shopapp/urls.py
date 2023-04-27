from django.urls import path
from .views import ShopIndexView, GroupsListView, products_list, orders_list, create_product, ProductDetailsView
app_name = 'shopapp'

urlpatterns = [
    path('', ShopIndexView.as_view(), name = 'index'),
    path("groups/", GroupsListView.as_view(), name = "groups_list"),
    path('products/', products_list, name= 'products_list'),
    path('products/<int:pk>/', ProductDetailsView.as_view(), name='products_details'),
    path('orders/', orders_list, name = 'orders-list'),
    path('products/create/', create_product, name = 'product-create'),
]
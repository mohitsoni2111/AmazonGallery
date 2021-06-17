from django.urls import path, include
from .views import ProductList, CategoryViewSet, SellerViewSet, ProductListAPIView
from rest_framework.routers import DefaultRouter

"""
Binding ViewSets to URLs explicitly
"""
# Method 1 (Manual Binding)
category_list = CategoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

category_detail = CategoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

# Method 2 (Using Routers)
router = DefaultRouter(trailing_slash=False)
router.register('sellers', SellerViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('products/', ProductList.as_view()),
    path('products-filter/', ProductListAPIView.as_view()),
    # path('categories', CategoryViewSet.as_view()),
    path('categories/', category_list, name='category_list'),
    path('categories/<int:pk>/', category_detail, name='category_detail'),
    # path('sellers', SellerViewSet.as_view()),
]

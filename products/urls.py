from django.urls import path , include
from .views import ProductList, ProductDetail, BrandList, BrandDetail, CategoryList,CategoryDetail,add_review

from .api import ProductListAPI,ProductDetailAPI,CategoryListAPI,CategoryDetailAPI,BrandListAPI,BrandDetailAPI,ProductViewSet

app_name = "products"

from rest_framework import routers

router = routers.DefaultRouter()
router.register('myproducts',ProductViewSet)

urlpatterns = [
    # path('testing/' , product_list),
    # Frontend CBVs
    path("", ProductList.as_view(), name="product_list"),
    
    path("<slug:slug>/", ProductDetail.as_view(), name="product_detail"),
    path("<slug:slug>/review_add", add_review, name="add_review"),
    
    path("<int:pk>", ProductDetail.as_view(), name="product_detail"),
    path("<slug:slug>/review_add", add_review , name="add_review"),
    
    path("brands", BrandList.as_view(), name="brand_list"),
    path("brands/<int:pk>", BrandDetail.as_view(), name="brand_detail"),
    path("category", CategoryList.as_view(), name="category_list"),
    path("category/<int:pk>", CategoryDetail.as_view(), name="category_detail"),
    
    
    # path('api/list' , product_list_api),
    # path('api/list/<int:id>' , product_detail_api),
    # APIs
    
    
    path("api/list/cbv", ProductListAPI.as_view()),
    path("api/list/cbv/<int:pk>", ProductDetailAPI.as_view()),
    
    path("api/category", CategoryListAPI.as_view()), 
    path("api/category/<int:pk>", CategoryDetailAPI.as_view()),
   
    path("api/brand", BrandListAPI.as_view()), 
    path("api/brand/<int:pk>", BrandDetailAPI.as_view()),
    
      
    path('myapi/', include(router.urls))  
]



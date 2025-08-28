from rest_framework.response import Response
from .serializers import ProductSerializers ,CategorySerializer , BrandSerializer , CategoryDetailSerializer ,BrandDetailSerializer 
from .models import Product , Category , Brand
from rest_framework.decorators import api_view


#from django.contrib.auth.models import User
#from products.serializers import UserSerializer
import django_filters.rest_framework
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated





"""
@api_view(['GET'])
def product_list_api(request):
    products = Product.objects.all()
    data = ProductSerializers(products ,many=True).data
    return Response ({'Success':True, 'Product List': data})




@api_view(['GET'])
def product_detail_api(request,id):
    produts = Product.objects.get(id=id)
    data = ProductSerializers(produts).data
    return Response ({'Success':True, 'Product': data})
"""

#class UserListView(generics.ListAPIView):
    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    #filter_backends = [django_filters.rest_framework.DjangoFilterBackend]

#product list , detail

class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name', 'price', 'brand']  # الحقول اللي عايز تظهرها في الـ API
    permission_classes = [IsAuthenticated]


class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()


# category list , detail

class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
    
class CategoryDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    
    
    
# brand list , detail

class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()    
    
    
    
class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandDetailSerializer
    queryset = Brand.objects.all()    
    
    

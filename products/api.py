from rest_framework.response import Response
from .serializers import ProductSerializers
from .models import Product
from rest_framework.decorators import api_view


'''
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
'''



from rest_framework import generics


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    
    
    
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    

    
















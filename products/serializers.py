from rest_framework import serializers
from .models import Product , Brand , Category

#class UserSerializer(serializers.ModelSerializer):
   # class Meta:
       # model = User
        # الحقول اللي عايز تظهرها في الـ API
        #fields = ['id', 'username', 'email', 'first_name', 'last_name']
        


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name','image']


class BrandSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    class Meta:
        model = Brand
        fields = ['name','image','category']



class ProductSerializers(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    
    
    price_with_discount = serializers.SerializerMethodField()
    
    #brand = serializers.StringRelatedField()
    #category = serializers.StringRelatedField()
    
    def get_price_with_discount(self,product):
        return (product.price - product.price *.10)
    
    
    class Meta:
        model = Product
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ['name','image']


class CategoryDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializers(source='product_category',many=True)
    
    class Meta:
        model = Category
        fields = ['name','image','products']


class BrandDetailSerializer(serializers.ModelSerializer):
    products = ProductSerializers(source='product_brand',many=True)
    category = serializers.StringRelatedField()
    class Meta:
        model = Brand
        fields = ['name','image','category','products']

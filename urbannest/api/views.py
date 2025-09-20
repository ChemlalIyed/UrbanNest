from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework import status
from .serializers import ProductsSerializer,HomeSerializer,CartSerializer,OrdersSerializer,UserSerializer,CategorysSerializer,PhoneSerializer
from .models import Products,Homepage_image,Cart,Order,User,Category,Phone
import requests
class ProductsView(ModelViewSet):
    queryset=Products.objects.all()
    serializer_class=ProductsSerializer

class CategorysView(ListAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorysSerializer

class HomeView(ModelViewSet):
    queryset=Homepage_image.objects.all()
    serializer_class=HomeSerializer    

class OrdersView(ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrdersSerializer   
    def  get_queryset(self):
        token = self.request.query_params.get('token')
        print(token)
        if token:
            return Order.objects.filter(token=token).first()
        return super().get_queryset() 

class UserView(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class BanneUserView(APIView):
   def get(self,request):
      try :
        user=User.objects.filter(banned=True)
        ser = UserSerializer(user,many=True)
        return Response(ser.data)
      except Exception as e  :
       return Response({'error':str(e)})
    
   def post(self,request):
      try :
        token = request.data.get("token")
        method = request.data.get("method")
        user=User.objects.get(token=token)
        if not user.banned and not method:
           user.banned=True
           user.save()
        if  user.banned and method:
           user.banned=False
           user.save()   
        return Response({"Saccses":"1"})
      except Exception as e  :
       return Response({'error':str(e)})
      

class Message_api(APIView):
    def get(self,request,text):
        token = "8008497740:AAHvv4KhZsFTo7xdrfesVPQTMH3Gm6bOX1E"
        chat_id = "-1002603747015"
        url = f"https://api.telegram.org/bot8008497740:AAHvv4KhZsFTo7xdrfesVPQTMH3Gm6bOX1E/sendMessage?chat_id=-1002603747015&text={text}"
        requests.get(url)
        return Response({"sccess":1})   
class Cart_View(ModelViewSet):
    queryset=Cart.objects.all().order_by("product")
    serializer_class=CartSerializer
    def  get_queryset(self):
        token = self.request.query_params.get('token')
        print(token)
        if token:
            return Cart.objects.filter(token=token).order_by("product")
        return super().get_queryset()
class Like(APIView):
    def get(self,request,id,token,i):
        product=Products.objects.get(id=id)
        print(bool(i))
        
        if i==1 and token not in product.likers:
          product.likers.append(token)
          product.like=max(0,product.like+1)
          product.save()
          return Response({"like":"true"},status=status.HTTP_200_OK)
        elif i==0 and token in product.likers:
         product.likers.remove(token)
         product.like=max(0,product.like-1)
         product.save()
         return Response({"like":"true"},status=status.HTTP_200_OK)
        elif i==2 and token in product.likers:
           return Response({"liked":"true"},status=status.HTTP_200_OK)
        elif i==2 and token not in product.likers:
           return Response({"liked":"false"},status=status.HTTP_200_OK)
        else:
         return Response({"like":"false"},status=status.HTTP_400_BAD_REQUEST)
        
class PhoneView(ModelViewSet):
    queryset=Phone.objects.all()
    serializer_class=PhoneSerializer  
    http_method_names=["post"]   

from django.shortcuts import render
from  rest_framework .decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializer import CategorySerializer
from rest_framework.exceptions import ValidationError
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView,ListAPIView

# Create your views here.

class CategoryList(APIView):
    def get(self,request):
        category = Category.objects.all()
        serializer = CategorySerializer(category,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status= status.HTTP_201_CREATED)
    
class CagegoryDetail(APIView):
    def get(self,request,pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    def put(self,request,pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self,request,pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({"message deleted"},status=status.HTTP_204_NO_CONTENT)
    
# @api_view(['GET','POST'])
# def category_list(request):
#     if request.method == 'GET':
#         category = Category.objects.all()
#         serializer = CategorySerializer(category, many=True)
#         return Response(serializer.data)


#     elif request.method == 'POST':
#         serializer = CategorySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    
# @api_view(['GET','PUT','DELETE'])
# def category_detail(request, pk):
#     category = Category.objects.get(pk=pk)
#     if request.method == 'GET':
       
#         serializer = CategorySerializer(category)
#         return Response(serializer.data)
#     elif request.method  == 'PUT':
#         serializer = CategorySerializer(category,data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#     elif request.method == 'DELETE':
#         category.delete()
#         return Response({"message deleted"},status=status.HTTP_204_NO_CONTENT)
    
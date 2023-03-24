from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CategorySerializer
from .models import Category

# Create your views here.
@api_view(['GET'])
def index(request):
    print(request)
    return Response("All Praise to ALLAH, the only Perfect!")

@api_view(['POST'])
def addCategory(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response("Category added successfully")


@api_view(['GET'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
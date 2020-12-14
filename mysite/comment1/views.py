from django.shortcuts import render
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status

from comment1.models import Comment1
from comment1.serializers import Comment1Serializer

@csrf_exempt
def comment1_list(request):
    if request.method == 'GET':
        comment1 = Comment1.objects.all()
        comment1_serializer = Comment1Serializer(comment1, many=True)
        return JsonResponse(comment1_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        comment1_data = JSONParser().parse(request)
        comment1_serializer = Comment1Serializer(data=comment1_data)
        if comment1_serializer.is_valid():
            comment1_serializer.save()
            return JsonResponse(comment1_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(comment1_serializer.errors, status=status.HTTP_400_BAD_REQUES)

# Create your views here.

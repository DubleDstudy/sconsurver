from django.shortcuts import render
from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from contents.models import Contents
from contents.serializers import ContentsSerializer
# Create your views here.

@csrf_exempt
def contents_list(request):
    if request.method == 'GET':
        contents = Contents.objects.all()
        contents_serializer = ContentsSerializer(contents, many=True)
        return JsonResponse(contents_serializer.data, safe=False)
        # In order to serialize objects, we must set 'safe=False'

    elif request.method == 'POST':
        contents_data = JSONParser().parse(request)
        contents_serializer = ContentsSerializer(data=contents_data)
        if contents_serializer.is_valid():
            contents_serializer.save()
            return JsonResponse(contents_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(contents_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

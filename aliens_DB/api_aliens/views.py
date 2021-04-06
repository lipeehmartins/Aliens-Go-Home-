from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import History
from .serializers import HistorySerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import  mixins
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

class HistoryViewSet(viewsets.ModelViewSet):
    serializer_class = HistorySerializer
    queryset = History.objects.all()

@api_view(['GET', 'POST'])
def history_list(request):

    if request.method == 'GET':
        historys = History.objects.all()
        serializer = HistorySerializer(historys, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HistorySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data, status=status.HTTP_201_CREATED)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''@api_view(['GET', 'PUT', 'DELETE'])
def history_detail(request, pk):
    try:
        history = history.objects.get(pk=pk)

    except history.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = HistorySerializer(history)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data)
        return  Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        history.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)'''
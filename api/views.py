import json
from .constants import clQuestionsList
from django.shortcuts import render
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.views import APIView
from django.views import View


class fnBlackBoxAPI(APIView):
    def get(self,request,pk):
        if clQuestionsList.get(pk):
            fnFunctionName = clQuestionsList[pk]
            try:
                params = request.GET.dict()
                output = fnFunctionName(*params.values())
            except Exception as e:
                return Response(data={'message':f'Got Error :{str(e)}'},status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(data={'output':output},status=status.HTTP_200_OK)
        else:
            data = {
                'message':"Looks like there is no such route exists"
            }
            return Response(data=data,status=status.HTTP_404_NOT_FOUND)
        
    def options(self, request, *args, **kwargs):
        headers = {
            'Allow': 'GET, OPTIONS', 
            'Custom-Header': 'Custom-Value', 
        }

        response = Response()
        for key, value in headers.items():
            response[key] = value

        return response
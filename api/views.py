from . import questions
from rest_framework import status
from .constants import clOptionsDict
from rest_framework.views import APIView
from rest_framework.response import Response

clQuestionsList = {
    "question1":questions.question1,
    "question2":questions.question2
}

class fnBlackBoxAPI(APIView):
    def get(self,request,pk):
        if clQuestionsList.get(pk):
            fnFunctionName = clQuestionsList[pk]
            try:
                params = request.GET.dict()
                output = fnFunctionName(**params)
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
        pk = kwargs.get('pk')
        
        if clOptionsDict.get(pk):
            clInputFormat = clOptionsDict.get(pk)
            clResponseData = {
                'name': pk,
                "description":"Options for the Black Box API",
                "renders":[
                    "application/json",
                    "text/html"
                ],
                "parses": [
                    "application/json",
                    "application/x-www-form-urlencoded",
                    "multipart/form-data"
                ],
                "actions":{
                    "GET":clInputFormat
                }
            }
        else:
            clResponseData = {
                'message': "Looks like there doesn't exist any route no options found",
            }
        
        headers = {
            'Allow': 'GET, OPTIONS',
            'Custom-Header': 'Custom-Value',
        }

        response = Response(data=clResponseData, headers=headers, status=status.HTTP_200_OK)
        return response
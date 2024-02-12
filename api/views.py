from . import questions
from rest_framework import status
from .constants import clOptionsDict
from rest_framework.views import APIView
from rest_framework.response import Response

clQuestionsList = {
    "question1":questions.question1,
    "question2":questions.question2,
    "question3":questions.question3,
    "question4":questions.question4,
    "question5":questions.question5,
    "question6":questions.question6,
    "question7":questions.question7,
    "question8":questions.question8,
    "question9":questions.question9,
    "question10":questions.question10,
    "question11":questions.question11,
    "question12":questions.question12,
    "question13":questions.question13,
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

        return Response(data=clResponseData, headers=headers, status=status.HTTP_200_OK)
    
class fnBlackBoxHints(APIView):
    def get(self,request,pk):
        if clQuestionsList.get(pk):
            print(pk)
        else:
            return Response(data={'message':'Looks like there no such question exists please try options'},status=status.HTTP_400_BAD_REQUEST)
            
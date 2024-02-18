from api.models import Solution
from . import questions
from rest_framework import status
from .constants import clOptionsDict
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .serializer import SolutionSerializer, UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

clQuestionsList = {
    "1":questions.question1,
    "2":questions.question2,
    "3":questions.question3,
    "4":questions.question4,
    "5":questions.question5,
    "6":questions.question6,
    "7":questions.question7,
    "8":questions.question8,
    "9":questions.question9,
    "10":questions.question10,
    "11":questions.question11,
    "12":questions.question12,
    "13":questions.question13,
}

class fnBlackBoxAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
        
        if clQuestionsList.get(pk):
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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        if clQuestionsList.get(pk):
            print(pk)
        else:
            return Response(data={'message':'Looks like there no such question exists please try options'},status=status.HTTP_400_BAD_REQUEST)
            
            
class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(data={
                'message':str(serializer.errors)
            },status=status.HTTP_400_BAD_REQUEST)
            
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        token_obj,_ = Token.objects.get_or_create(user=user)
        
        return Response(data={
            'token':str(token_obj)
        },status=status.HTTP_201_CREATED)
        
class SubmitQuestion(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,pk):
        if not clQuestionsList.get(pk):
            return Response(data={'message':'Looks like there no such question exists please try options'},status=status.HTTP_400_BAD_REQUEST)

        request.data['questionID'] = pk
        serializer = SolutionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        question_id = pk
        user = request.user
        try:
            existing_solution = Solution.objects.select_for_update().filter(
                user=user, questionID=question_id
            ).first()
            if existing_solution:
                existing_solution.code = serializer.validated_data['code']
                existing_solution.save()
                serializer = SolutionSerializer(existing_solution)
                return Response(data={'message':'data stored successfully'}, status=status.HTTP_200_OK)
            
            solution = serializer.save(user=user)
            serializer = SolutionSerializer(solution).data
            data = {
                'username':serializer['user']['username'],
                'questionID':serializer['questionID'],
                'code':serializer['code']
            }
            return Response(data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': 'Concurrent modification detected. Please try again.'}, status=status.HTTP_409_CONFLICT)
        
    def get(self,request,pk):
        if not clQuestionsList.get(pk):
            return Response(data={'message':'Looks like there no such question exists please try options'},status=status.HTTP_400_BAD_REQUEST)

        try:
            solution = Solution.objects.get(user=request.user, questionID=pk)
        except Exception as e:
            return Response(data={'message':'Solution not found for this user and question ID.'},status=status.HTTP_404_NOT_FOUND)

        serializer = SolutionSerializer(solution).data
        data = {
            'username':serializer['user']['username'],
            'questionID':serializer['questionID'],
            'code':serializer['code']
        }
        return Response(data,status=status.HTTP_200_OK)
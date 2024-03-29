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
import json
import traceback
from django.db import transaction
from django.http import JsonResponse

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
    # "12":questions.question12,
    # "13":questions.question13,
}

class fnBlackBoxAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        if clQuestionsList.get(pk):
            fnFunctionName = clQuestionsList[pk]
            try:
                params = request.GET.dict()
                print(params)
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
                # 'name': pk,
                # "description":"Options for the Black Box API",
                # "renders":[
                #     "application/json",
                #     "text/html"
                # ],
                # "parses": [
                #     "application/json",
                #     "application/x-www-form-urlencoded",
                #     "multipart/form-data"
                # ],
                # "actions":{
                #     "GET":clInputFormat
                # }
                'data':clInputFormat
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

class ListOfQuestion(APIView):
    def options(self, request):
        # Assuming questions is a list of dictionaries
        
        
        # Serialize questions to JSON
        serialized_questions = json.dumps([
    {"id": 1, "title": "Question 1", "points": 1},
    {"id": 2, "title": "Question 2", "points": 1},
    {"id": 3, "title": "Question 3", "points": 1},
    {"id": 4, "title": "Question 4", "points": 1},
    {"id": 5, "title": "Question 5", "points": 1},
    {"id": 6, "title": "Question 6", "points": 1},
    {"id": 7, "title": "Question 7", "points": 1},
    {"id": 8, "title": "Question 8", "points": 1},
    {"id": 9, "title": "Question 9", "points": 1},
    {"id": 10, "title": "Question 10", "points": 1},
    {"id": 11, "title": "Question 11", "points": 1},
    # {"id": 12, "title": "Question 12", "points": 1},
    # {"id": 13, "title": "Question 13", "points": 1}
]
)
        
        return JsonResponse(data={'questions': serialized_questions}, status=status.HTTP_200_OK)

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
            with transaction.atomic():
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
            line_number = traceback.extract_tb(e.__traceback__)[-1].lineno
            return Response({'error': f'Concurrent modification detected. Please try again.',"e":str(e),"line_number":line_number}, status=status.HTTP_409_CONFLICT)
        
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
    
class UserQuestionsDetails(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print("Hey")
        user = request.user
        solutions = Solution.objects.filter(user=user)
        serializer = SolutionSerializer(solutions,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

class LoginUser(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(data={
                "message":"user not found"
            }, status=status.HTTP_400_BAD_REQUEST)
        
        token_obj, _ = Token.objects.get_or_create(user=user)
        
        return Response(data={
            'token': str(token_obj),
            'email': str(user)  # Assuming you want to return the user's email
        }, status=status.HTTP_201_CREATED)
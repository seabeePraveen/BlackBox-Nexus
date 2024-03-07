from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('question/all/', views.ListOfQuestion.as_view(),name="listOfAllQuestions"),
    path('question/<str:pk>/',views.fnBlackBoxAPI.as_view(),name='apiView'),
    path('auth/register/',views.RegisterUser.as_view(),name='registerUser'),
    path('auth/login/',obtain_auth_token,name='loginUser'),
    path('question/<str:pk>/hint/',views.fnBlackBoxHints.as_view(),name='hintsView'),
    path('solution/<str:pk>/',views.SubmitQuestion.as_view(),name='submitQuestion')
    
]

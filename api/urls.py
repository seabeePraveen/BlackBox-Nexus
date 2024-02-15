from django.urls import path
from . import views


urlpatterns = [
    path('question/<str:pk>/',views.fnBlackBoxAPI.as_view(),name='apiView'),
    path('user-register/',views.RegisterUser.as_view(),name='registerUser'),
    path('question/<str:pk>/hint/',views.fnBlackBoxHints.as_view(),name='hintsView'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/',views.fnBlackBoxAPI.as_view(),name='apiView'),
    path('<str:pk>/hint/',views.fnBlackBoxHints.as_view(),name='hintsView'),
]

from django.urls import path,include
from .views import *
urlpatterns = [
    path('category/', CategoryList.as_view()),
    path('category/<pk>/', CagegoryDetail.as_view()),
]

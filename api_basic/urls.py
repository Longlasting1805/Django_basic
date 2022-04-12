from django.urls import path
from .views import article_list, article_detail, articleApiView, articleDetailApi, GenericApiView

urlpatterns = [
    # path('article/', article_list),
    path('article/', articleApiView.as_view()),
    # path('detail/<int:pk>/', article_detail)
    path('detail/<int:id>/', articleDetailApi.as_view()),
    path('generic/article/', GenericApiView.as_view())
]

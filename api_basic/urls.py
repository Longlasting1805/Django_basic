from django.urls import path, include
from .views import article_list, article_detail, articleApiView, articleViewSet, articleDetailApi, GenericApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', articleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/ ', include(router.urls)),
    # path('article/', article_list),
    path('article/', articleApiView.as_view()),
    # path('detail/<int:pk>/', article_detail)
    path('detail/<int:id>/', articleDetailApi.as_view()),
    path('generic/article/<int:id>/', GenericApiView.as_view())
]

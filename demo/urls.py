from django.urls import path, include
from . import views
from .views import Another, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('firstFunction', views.first),
    path('secondFunction', views.second),
    path('thirdFunction', views.third),
    path('fourthFunction', views.fourth),
    path('anotherFunction', Another.as_view()),
    path('', include(router.urls)),
]

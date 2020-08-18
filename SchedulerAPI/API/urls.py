from django.urls import include,path
from .views import TaskViewSet,server_check
from rest_framework.routers import DefaultRouter



OneEndpointRouter=DefaultRouter()
OneEndpointRouter.register('',viewset=TaskViewSet)
urlpatterns = [
    path('tasks/', include(OneEndpointRouter.urls)),
    path('ping/',server_check)
]
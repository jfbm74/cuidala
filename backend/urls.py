from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

#router = DefaultRouter()
#router.register(r'api/v1/user', UserViewSet, basename="user_list")
#urlpatterns = router.urls
urlpatterns = [
    path('theuser/', index, name = 'user_list'),
]

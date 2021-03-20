from django.urls import path, include
from rest_framework import routers

from main.views import ListViewSet

router = routers.SimpleRouter()
router.register('todos', ListViewSet, basename='main')

urlpatterns = [

]

urlpatterns += router.urls

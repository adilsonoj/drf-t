from django.contrib import admin
from django.urls import path, include
from website.views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='Posts')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

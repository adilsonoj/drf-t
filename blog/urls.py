from django.contrib import admin
from django.urls import path, include
from website.views import PostViewSet
from conta.views import AccountViewSet, ClientViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', PostViewSet, basename='Posts')
router.register('accounts', AccountViewSet, basename='accounts')
router.register('clients', ClientViewSet, basename='clients')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

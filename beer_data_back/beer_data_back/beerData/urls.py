from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import SimpleRouter

from .views import *

router = SimpleRouter()

urlpatterns = [
    url(r'', include(router.urls)),
    path('BeerDataPoster/', BeerView),


]

"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
app_name = 'main'
from .views import *
from rest_framework import routers


urlpatterns = [


]


router = routers.SimpleRouter()
router.register(r'upload-lapbook', BlogsViewSet)
router.register(r'upload-abstract', AbstractViewSet)
router.register(r'upload-holiday', HolidayViewSet)
router.register(r'upload-registrarion', RegistrationViewSet)
router.register(r'upload-games', GamesViewSet)
router.register(r'upload-crafts', CraftsViewSet)
router.register(r'upload-contest', ContestsViewSet)
router.register(r'upload-development', DevelopmentViewSet)


router.register(r'ContestsReviews', ContestsReviews)
router.register(r'GamesReviews', GamesReviews)
router.register(r'DevelopmentReviews', DevelopmentReviews)
router.register(r'ImagesReviews', ImagesReviews)
router.register(r'HolidayReviews', HolidayReview)
router.register(r'RegistrationReviews', RegistrationReview)
router.register(r'LapbookReviews', LapbookReviews)
router.register(r'CraftsReviews', CraftsReviews)





urlpatterns = router.urls
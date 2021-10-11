from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from rest_framework import viewsets
from .serializers import *
from .models import Lapbook
from rest_framework.response import Response
from .serializers import *
class BlogsViewSet(viewsets.ModelViewSet):
    serializer_class = BlogsSerializer
    queryset = Lapbook.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)


class AbstractViewSet(viewsets.ModelViewSet):
    serializer_class = AbstractSerializer
    queryset = Abstract.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)


class HolidayViewSet(viewsets.ModelViewSet):
    serializer_class = HolidaySerializer
    queryset = Holiday.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)


class DevelopmentViewSet(viewsets.ModelViewSet):
    serializer_class = DevelopmentSerializer
    queryset = Development.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)

class RegistrationViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = Holiday.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)

class CraftsViewSet(viewsets.ModelViewSet):
    serializer_class = CraftsSerializer
    queryset = Crafts.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)

class GamesViewSet(viewsets.ModelViewSet):
    serializer_class = GamesSerializer
    queryset = Games.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)





class ContestsViewSet(viewsets.ModelViewSet):
    serializer_class = ContestsSerializer
    queryset = Contests.objects.all()

    def create(self, request, *args, **kwargs):
        instance_data = request.data
        data = {key: value for key, value in instance_data.items()}
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        if request.FILES:
            photos = dict((request.FILES).lists()).get('photos', None)
            if photos:
                for photo in photos:
                    photo_data = {}
                    photo_data["blogs"] = instance.pk
                    photo_data["image"] = photo
                    photo_serializer = ImageSerializer(data=photo_data)
                    photo_serializer.is_valid(raise_exception=True)
                    photo_serializer.save()

        return Response(serializer.data)

    def likes(self,request,pk):
        post = get_object_or_404(Contests, id=request.POST.get('contest_id'))
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('likes', args=[str(pk)]))



class ContestsReviews(viewsets.ModelViewSet):
    queryset = Reviews_Contests.objects.all()
    serializer_class = ReviewsSerializer

class GamesReviews(viewsets.ModelViewSet):
    queryset = Reviews_Games.objects.all()
    serializer_class = ReviewsSerializer

class AbstractReviews(viewsets.ModelViewSet):
    queryset = Reviews_Abstract.objects.all()
    serializer_class = ReviewsSerializer

class DevelopmentReviews(viewsets.ModelViewSet):
    queryset = Reviews_Development.objects.all()
    serializer_class = ReviewsSerializer

class CraftsReviews(viewsets.ModelViewSet):
    queryset = Reviews_Crafts.objects.all()
    serializer_class = ReviewsSerializer

class ImagesReviews(viewsets.ModelViewSet):
    queryset = Reviews_Images.objects.all()
    serializer_class = ReviewsSerializer

class LapbookReviews(viewsets.ModelViewSet):
    queryset = Reviews_Lapbook.objects.all()
    serializer_class = ReviewsSerializer

class HolidayReview(viewsets.ModelViewSet):
    queryset = Reviews_Holiday.objects.all()
    serializer_class = ReviewsSerializer

class RegistrationReview(viewsets.ModelViewSet):
    queryset = Reviews_Registration.objects.all()
    serializer_class = ReviewsSerializer
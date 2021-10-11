from rest_framework import serializers
from .models import Lapbook, LapbookImage
from .models import *
class ImageSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()


    def get_reviews(self,obj):
        reviews = Reviews_Images.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data

    class Meta:
        model = LapbookImage
        fields = ['task', 'image',]




class BlogsSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_photos(self, obj):
        photos = LapbookImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data


    def get_reviews(self,obj):
        reviews = Reviews_Lapbook.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data


    class Meta:
        model = Lapbook
        fields = "__all__"

class AbstractImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = AbstractImage
        fields = ['task', 'image',]


class AbstractSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()


    def get_photos(self, obj):
        photos = AbstractImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data


    def get_reviews(self,obj):
        reviews = Reviews_Abstract.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data

    class Meta:
        model = Abstract
        fields = '__all__'


class DevelopmentImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = DevelopmentImage
        fields = ['task', 'image',]


class DevelopmentSerializer(serializers.ModelSerializer):

    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_photos(self, obj):
        photos = DevelopmentImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data


    def get_reviews(self,obj):
        reviews = Reviews_Development.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data

    class Meta:
        model = Development
        fields = '__all__'


class HolidayImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidayImage
        fields = ['task', 'image', ]


class HolidaySerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_photos(self, obj):
        photos = HolidayImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data



    def get_reviews(self,obj):
        reviews = Reviews_Holiday.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data


    class Meta:
        model = Holiday
        fields = '__all__'



class RegistrationImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationImage
        fields = ['task', 'image', ]


class RegistrationSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()
    def get_photos(self, obj):
        photos = RegistrationImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data



    def get_reviews(self,obj):
        reviews = Reviews_Registration.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data


    class Meta:
        model = Registration
        fields = '__all__'

class CraftsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CraftsImage
        fields = ['task', 'image', ]


class CraftsSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_photos(self, obj):
        photos = CraftsImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data

    def get_reviews(self,obj):
        reviews = Reviews_Crafts.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data



    class Meta:
        model = Crafts
        fields = '__all__'



class GamesImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GamesImage
        fields = ['task', 'image', ]


class GamesSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_photos(self, obj):
        photos = GamesImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data


    def get_reviews(self,obj):
        reviews = Reviews_Games.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data

    class Meta:
        model = Games
        fields = '__all__'


class ContestsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContestsImage
        fields = ['task', 'image', ]


class ReviewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews_Contests
        fields = '__all__'


class ContestsSerializer(serializers.ModelSerializer):
    photos = serializers.SerializerMethodField()
    reviews = serializers.SerializerMethodField()

    def get_photos(self, obj):
        photos = ContestsImage.objects.filter(task=obj)
        return ImageSerializer(photos, many=True, read_only=False).data

    def get_reviews(self,obj):
        reviews = Reviews_Contests.objects.filter(task=obj)
        return ReviewsSerializer(reviews, many=True, read_only=False).data

    def get_likes(self):
        return self.likes.count()

    class Meta:
        model = Contests
        fields = '__all__'
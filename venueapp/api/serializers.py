from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from venueapp.models import (
    PopularPlace, FeaturedPlace,FavoriteList, BestTemplate, OurService, 
    PricingTable, Include, SocialMedia, SiteSettings
    )

class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)
    class Meta:
        model = User
        fields = ("username", "password")

    def validate(self, data):
        validate_password(data['password'])
        return data
    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]

        user = User.objects.create_user(
            username = username,
            password = password
        )
        return user
    
class PopularPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularPlace
        fields = "__all__"

class FeaturedPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedPlace
        fields = "__all__"

class FavoriteListSeializer(serializers.ModelSerializer):
    featured_place = FeaturedPlaceSerializer()
    user = UserCreateSerializer()
    class Meta:
        model = FavoriteList
        fields ="__all__"

class FavoriteListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteList
        fields = ("featured_place")

class BestTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestTemplate
        fields = "__all__"

class OurServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurService
        fields = "__all__"

class IncludeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Include
        fields = "__all__"

class PricingTableSerializer(serializers.ModelSerializer):
    includes = IncludeSerializer(many=True)
    class Meta:
        model = PricingTable
        fields = "__all__"

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = "__all__"
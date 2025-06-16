from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User
from venueapp.api.serializers import (
    UserCreateSerializer, PopularPlaceSerializer, FeaturedPlaceSerializer,
    FavoriteListSeializer, FavoriteListCreateSerializer, BestTemplateSerializer, OurServiceSerializer, 
    PricingTableSerializer, IncludeSerializer, SocialMediaSerializer, SiteSettingsSerializer
    )
from venueapp.models import (
    PopularPlace, FeaturedPlace, FavoriteList, BestTemplate, OurService,
    PricingTable, Include, SocialMedia, SiteSettings
    )
class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

class PopularPlaceListAPIView(ListAPIView):
    queryset = PopularPlace.objects.all()
    serializer_class = PopularPlaceSerializer

class FeaturedPlaceListAPIView(ListAPIView):
    queryset = FeaturedPlace.objects.all()
    serializer_class = FeaturedPlaceSerializer

class FeaturedPlaceRetrieveAPIView(RetrieveAPIView):
    queryset = FeaturedPlace.objects.all()
    serializer_class = FeaturedPlaceSerializer
    lookup_field = 'id'

class UserFavoriteListListAPIView(ListAPIView):
    def get_queryset(self):
        return FavoriteList.objects.filter(
            user = self.request.user
        )
    serializer_class = FavoriteListSeializer
    permission_classes = (IsAuthenticated, )

class FavoriteListListAPIView(ListAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListSeializer
    permission_classes = (IsAdminUser, )

class FavoriteListCreateAPIView(CreateAPIView):
    queryset = FavoriteList.objects.all()
    serializer_class = FavoriteListCreateSerializer
    permission_classes = (IsAuthenticated, )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

class BestTemplateListAPIView(ListAPIView):
    queryset = BestTemplate.objects.all()
    serializer_class = BestTemplateSerializer

class OurServiceListAPIView(ListAPIView):
    queryset = OurService.objects.all()
    serializer_class = OurServiceSerializer

class PricingTableListAPIView(ListAPIView):
    queryset = PricingTable.objects.all()
    serializer_class = PricingTableSerializer

class SocialMediaListAPIView(ListAPIView):
    queryset = SocialMedia.objects.all()
    serializer_class = SocialMediaSerializer

class SiteSettingListAPIView(ListAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer
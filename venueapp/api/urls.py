from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from venueapp.api import views

urlpatterns = [
    path('user-create/', views.UserCreateAPIView.as_view()),
    path('popularplace-list/', views.PopularPlaceListAPIView.as_view()),
    path('featuredplace-list/', views.FeaturedPlaceListAPIView.as_view()),
    path('featured-retrieve/<id>/', views.FeaturedPlaceRetrieveAPIView.as_view()),
    path('user-favoritelist/', views.UserFavoriteListListAPIView.as_view()),
    path('favoritelist-create/', views.FavoriteListCreateAPIView.as_view()),
    path('favoritelist/', views.FavoriteListListAPIView.as_view()),
    path('besttemplate-list/', views.BestTemplateListAPIView.as_view()),
    path('ourservice-list/', views.OurServiceListAPIView.as_view()),
    path('pricingtable-list/', views.PricingTableListAPIView.as_view()),
    path('socialmedia-list/', views.SocialMediaListAPIView.as_view()),
    path('sitesettings-list/', views.SiteSettingListAPIView.as_view())
]
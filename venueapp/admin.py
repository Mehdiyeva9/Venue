from django.contrib import admin
from venueapp.models import (
    PopularPlace, FeaturedPlace,FavoriteList, BestTemplate, OurService, 
    PricingTable, Include, SocialMedia, SiteSettings
    )

admin.site.register(PopularPlace)
admin.site.register(FeaturedPlace)
admin.site.register(FavoriteList)
admin.site.register(BestTemplate)
admin.site.register(OurService)
admin.site.register(PricingTable)
admin.site.register(Include)
admin.site.register(SocialMedia)
admin.site.register(SiteSettings)
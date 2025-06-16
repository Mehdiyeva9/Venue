from django.db import models
from django.contrib.auth.models import User

class PopularPlace(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='places_images/')
    listing = models.IntegerField(default=0)

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
class FeaturedPlace(models.Model):
    CATEGORY = (
        ('one' , 'one'),
        ('two' , 'two'),
        ('three' , 'three')
    )
    name = models.CharField(max_length=15)
    cotegory = models.TextField(choices=CATEGORY)
    image = models.ImageField(upload_to='place_images/')
    text = models.TextField()
    date = models.DateField()
    raiting = models.FloatField(default=0)


    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
class FavoriteList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_favorites')
    featured_place = models.ForeignKey(FeaturedPlace, on_delete=models.CASCADE, related_name="favorites")
    
class BestTemplate(models.Model):
    icon = models.TextField()
    title = models.CharField(max_length=20)
    content = models.TextField()

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.title

class OurService(models.Model):
    title = models.CharField(max_length=15)
    content = models.TextField()

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.title
    
class Include(models.Model):
    name = models.TextField()

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
class PricingTable(models.Model):
    name = models.CharField(max_length=15)
    price = models.FloatField(default=0)
    period = models.TextField()
    includes = models.ManyToManyField(Include, related_name="pricing_tables")

    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.name
    
class SocialMedia(models.Model):
    icon = models.TextField(blank=True, null=True)
    link = models.URLField(max_length=200, blank=True, null=True)
    
    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.icon
    
class SiteSettings(models.Model):
    logo = models.ImageField(upload_to="settings_images/", blank=True, null=True)
    banner_title = models.TextField(blank=True, null=True)
    banner_content = models.TextField(blank=True, null=True)
    p_place_title = models.TextField(blank=True, null=True)
    f_place_title = models.TextField(blank=True, null=True)
    services_title = models.TextField(blank=True, null=True)
    services_subtitle = models.TextField(blank=True, null=True)
    services_content = models.TextField(blank=True, null=True)
    video_title = models.TextField(blank=True, null=True)
    video = models.FileField(upload_to="settings_images/", blank=True, null=True)
    pricing_table_title = models.TextField(blank=True, null=True)
    contact_us_title = models.TextField(blank=True, null=True)
    venue_text = models.TextField(blank=True, null=True)
    contact_subtitle = models.TextField(blank=True, null=True)
    contact_content = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
    email = models.EmailField(max_length=256, blank=True, null=True)
    adress = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Settings'
        verbose_name_plural = 'Settings'
    
    def __str__(self):
        return 'Settings'
    
    def save(self, *args, **kwargs):
        if not self.id and SiteSettings.objects.exists():
            pass
        return super(SiteSettings, self).save(*args, **kwargs)
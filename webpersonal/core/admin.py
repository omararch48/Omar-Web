from django.contrib import admin
from .models import SocialNetworks


class CoreSocialNetworks(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

# Register your models here.
admin.site.register(SocialNetworks, CoreSocialNetworks)
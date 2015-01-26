from django.contrib import admin
from image_cropping import ImageCroppingMixin
from . import models


class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(models.Profile, ProfileAdmin)
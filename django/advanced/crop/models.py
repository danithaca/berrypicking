from django.db import models
from image_cropping.fields import ImageCropField, ImageRatioField


class Profile(models.Model):
    avatar = ImageCropField()
    cropping = ImageRatioField('avatar', '200x200')
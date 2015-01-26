from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import DetailView, UpdateView, FormView
from . import models
from image_cropping import ImageCropWidget


class ProfileView(DetailView):
    model = models.Profile
    template_name = 'crop/view.html'


class ProfileForm(ModelForm):
    class Meta:
        model = models.Profile
        fields = ['avatar', 'cropping']
        widgets = {'avatar': ImageCropWidget,}


# class EditView(UpdateView):
#     model = models.Profile
#     # template_name = 'crop/profile_form.html'
#     fields = ['avatar']


class EditView(FormView):
    form_class = ProfileForm
    template_name = 'crop/edit.html'
    success_url = '/'


def dummy(request):
    return HttpResponse('Home')
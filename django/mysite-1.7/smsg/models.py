from django.db import models
from django.forms import ModelForm
#from django.forms import modelform_factory


class Message(models.Model):
    body = models.TextField()

    def __str__(self):
        return self.body


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ('body',)
#MessageForm = modelform_factory(Message, fields=('body'))
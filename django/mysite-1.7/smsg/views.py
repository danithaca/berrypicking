from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
from django.views import generic
from smsg.models import Message, MessageForm


class ListView(generic.ListView):
    model = Message
    template_name = 'smsg/list.jinja2'


class EditView(generic.UpdateView):
    model = Message
    template_name = 'smsg/edit.jinja2'
    success_url = reverse_lazy('smsg:list')


def add(request):
    #return HttpResponse('ok.')
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('smsg:list')
        #return HttpResponseRedirect('/smsg')
    else:
        form = MessageForm()
        # this has to have "request" as input, otherwise csrf_token would not be included.
    return render(request, 'smsg/add.jinja2', {'form': form})
from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import RequestContext, loader
from django.views import generic
from django.utils import timezone
from .models import Poll, Choice


def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]

    # approach 1:

    # template = loader.get_template('polls/index.html')
    # context = RequestContext(request, {
    #     'latest_poll_list': latest_poll_list,
    # })
    # return HttpResponse(template.render(context))

    # approach 2: a shortcut

    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

    # return HttpResponse("Hello, world. You're at the poll index.")


def detail(request, poll_id):
    #return HttpResponse("You're looking at poll %s." % poll_id)

    # approach 1:
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404

    # approach 2: a shortcut
    poll = get_object_or_404(Poll, pk=poll_id)

    return render(request, 'polls/detail.html', {'poll': poll})


def results(request, poll_id):
    # return HttpResponse("You're looking at the results of poll %s." % poll_id)
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})


def vote(request, poll_id):
    # return HttpResponse("You're voting on poll %s." % poll_id)
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
            })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # daniel: reverse() is to find the url of the view
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


#################################### below is the shortcut version ################################


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    # for test purposes in tutorial part 5.
    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'
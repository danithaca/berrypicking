from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render


def demo(request):
    return render(request, 'demo/demo.html')


def demo_autocomplete(request, template_name='demo/autocomplete.html'):
    q = request.GET.get('q', '')
    context = {'q': q}

    queries = {
        'users': User.objects.filter(Q(username__icontains=q) | Q(first_name__icontains=q) | Q(last_name__icontains=q) | Q(email__icontains=q)).distinct()[:3]
    }

    context.update(queries)

    return render(request, template_name, context)
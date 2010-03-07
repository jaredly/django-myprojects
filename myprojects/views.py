# Create your views here.
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.http import Http404
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _

from myprojects.models import Project

def list_all(request):
    return render_to_response('myprojects/index.html', 
            {'projects':Project.objects.order_by('time')}, 
            RequestContext(request))

def view_one(request, slug):
    if not slug:
        return redirect(reverse('myprojects-list'))
    try:
        project = Project.objects.get(slug=slug)
    except Project.NotFoundException:
        raise Http404
    return render_to_response('myprojects/view.html', 
            {'project':project, 'slug':slug}, 
            RequestContext(request))


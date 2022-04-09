from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'imageparse/index.html'
    context_object_name = 'latest_question_list'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
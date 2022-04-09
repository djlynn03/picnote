from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .utils import image_intake
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'imageparse/index.html'
    context_object_name = 'latest_question_list'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        print(request.POST, request.FILES)
        final_image = image_intake(request.FILES['file'])
        # raise Exception("Not implemented")
        return render(request, self.template_name, {"output": final_image})
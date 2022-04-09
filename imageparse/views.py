from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
import base64
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

        from io import BytesIO

        buffered = BytesIO()
        final_image[0].save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        return render(request, 'imageparse/index.html', {'output': "data:image/png;base64," + img_str.decode('utf-8')})
        return render(request, self.template_name, {"output": final_image[0], "original": request.FILES['file']})
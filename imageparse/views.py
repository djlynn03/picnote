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

        if 'file' not in request.FILES:
            return JsonResponse({'error': 'No file uploaded'})
        try:
            final_image = image_intake(request.FILES['file'])
        except:
            return render(request, self.template_name, {'error': 'Invalid file type'})

        from io import BytesIO

        buffered = BytesIO()
        final_image[0].save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue())
        return render(request, self.template_name, {'output': "data:image/png;base64," + img_str.decode('utf-8')})
    
def upload(request, *args, **kwargs):
    pass
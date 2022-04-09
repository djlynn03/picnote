from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt
from PIL import Image

import base64
from .utils import image_intake

class IndexView(generic.ListView):
    template_name = 'imageparse/index.html'
    context_object_name = 'latest_question_list'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
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
    print(request.POST, request.FILES)
    from io import BytesIO
    buffered = BytesIO()
    
    image = request.FILES['image']
    image = image_intake(image)[0]
    image.save(buffered, format="JPEG")
    final_image = base64.b64encode(buffered.getvalue())
    return JsonResponse({'new_preview': "data:image/png;base64," + final_image.decode('utf-8')})
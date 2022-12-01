from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic import DetailView
from .forms import FaceForm
from .models import Face

def index(request):
    return render(request, 'facerecognition/index.html')

class FaceImage(TemplateView):
    form = FaceForm
    template_name = 'facerecognition/face_image.html'

    def post(self, request, *args , **kwargs):
        form = FaceForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            return HttpResponseRedirect(reverse_lazy('facerecognition:face_image_display', kwargs={'pk': obj.id}))
        context = self.get_context_data(form=form)
        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

class FaceImageDisplay(DetailView):
    model = Face
    template_name = 'facerecognition/face_image_display.html'
    context_object_name = 'face'
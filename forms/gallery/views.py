from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import GalleryUploadForm
from django.http import HttpResponseRedirect
from .models import Gallery


# Create your views here.

# def storage_file(file):
#     with open(f"forms/gallery_tmp/{file.name}", 'wb+') as new_file:
#         for chunk in file.chunks():
#             new_file.write(chunk)
#

# class GalleryView(View):
#     def get(self, request):
#         form = GalleryUploadForm()
#         return render(request, 'gallery/load_file.html', {'form': form})
#
#     def post(self, request):
#         form = GalleryUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # storage_file(form.cleaned_data['image'])
#             new_image = Gallery(image=form.cleaned_data['image']) #благодаря модели избавляемся от кода по сохранению картинки
#             new_image.save()
#             return HttpResponseRedirect('load_image')
#         return render(request, 'gallery/load_file.html', {'form': form})

class GalleryView(CreateView):
    model = Gallery
    fields = '__all__'
    template_name = 'gallery/load_file.html'
    success_url = 'load_image'


class ListGallary(ListView):
    model = Gallery
    template_name = 'gallery/list_file.html'
    context_object_name = 'records'

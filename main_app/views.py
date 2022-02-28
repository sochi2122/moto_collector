import uuid
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Motorcycle, Accessory, Photo
from .forms import MileForm

import boto3
import uuid

S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'motorcyclecollector227'

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def motorcycles_index(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, 'motorcycles/index.html', {'motorcycles': motorcycles})

def motorcycles_detail(request, motorcycle_id):
   motorcycle = Motorcycle.objects.get(id=motorcycle_id)
   mile_form = MileForm()

   accessories_motorcycle_doesnt_have = Accessory.objects.exclude(id__in = motorcycle.accessories.all().values_list('id'))

   return render(request, 'motorcycles/detail.html', {
       'motorcycle': motorcycle, 
       'mile_form': mile_form,
       'accessories': accessories_motorcycle_doesnt_have 
    })

def add_mile(request, motorcycle_id):
    
    form = MileForm(request.POST)
    # 2) valid input values
    if form.is_valid():
        # 3) save a copy of a new feeding instance in memory
        new_mile = form.save(commit=False)
        # 4) attach a reference to the cat that owns the feeding
        new_mile.motorcycle_id = motorcycle_id
        # 5) save the new feeding to the database
        new_mile.save()

    return redirect('detail', motorcycle_id=motorcycle_id)









def assoc_accessory(request, motorcycle_id, accessory_id):
    Motorcycle.objects.get(id=motorcycle_id).accessories.add(accessory_id)
    return redirect('detail', motorcycle_id=motorcycle_id)

def add_photo(request, motorcycle_id):
    # photo-file will be the "name" attribute on the <input type="file">
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, motorcycle_id=motorcycle_id)
            photo.save()

        except Exception as error:
            print('**************************')
            print("An error occured while uploading")
            print(error)

        # except:
        #     print('An error occurred uploading file to S3')
    return redirect('detail', motorcycle_id=motorcycle_id)

class MotorcycleCreate(CreateView):
    model = Motorcycle
    fields = ('model', 'brand', 'year', 'description')
   
   
   

class MotorcycleUpdate(UpdateView):
    model = Motorcycle
    fields = ('model', 'brand', 'year', 'description')

class MotorcycleDelete(DeleteView):
    model = Motorcycle
    success_url = '/motorcycles/'

class AccessoryCreate(CreateView):
    model = Accessory
    fields = ('name','model', 'brand')


class AccessoryUpdate(UpdateView):
    model = Accessory
    fields = ('name','model', 'brand')


class AccessoryDelete(DeleteView):
    model = Accessory
    success_url = '/accessories/'


class AccessoryDetail(DetailView):
    model = Accessory
    template_name = 'accessories/detail.html'


class AccessoryList(ListView):
    model = Accessory
    template_name = 'accessories/index.html'
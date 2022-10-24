from django.shortcuts import render, redirect
from .models import *

def add_image(request):
    if request.method == "POST":
        photo = request.FILES.get("photo")
        AdImage.objects.create(
            photo=photo
        )
    return redirect("dashboard")


def add_category(request):
    if request.method == "POST":
        name = request.POST.get("name")
        photo = request.FILES.get("photo")
        Category.objects.create(
            name=name,
            photo=photo
        )
    return redirect("dashboard")


def delete_image(request, pk):
  img = AdImage.objects.get(id=pk)
  img.delete()
  return redirect('dashboard')


def delete_category(request, pk):
  category = Category.objects.get(id=pk)
  category.delete()
  return redirect('dashboard')




def update_image(request, pk):
  image = AdImage.objects.get(id=pk)
  if request.method == 'POST':
      photo = request.FILES.get('photo')
  image.save(photo=photo)
  return redirect('dashboard')




def update_category(request, pk):
  category = Category.objects.get(id=pk)
  if request.method == 'POST':
      name = request.POST.get('name'),
      photo = request.FILES.get('photo')
  category.save(name=name, photo=photo)
  return redirect('dashboard')



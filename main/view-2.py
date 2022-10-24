from django.shortcuts import render, redirect
from .models import *


def add_region(request):
    if request.method == "POST":
        name = request.POST.get("name")
        Region.objects.create(
            name=name
        )
    return redirect("information")


def add_sub(request):
    if request.method == "POST":
        name = request.POST.get("name")
        category = request.POST.get("category")
        Subcategory.objects.create(
            name=name,
            category_id=category
        )
    return redirect("information")


def delete_region(request, pk):
  region = Region.objects.get(id=pk)
  region.delete()
  return redirect('index')


def delete_info(request, pk):
  info = Information.objects.get(id=pk)
  info.delete()
  return redirect('index')


def delete_sub(request, pk):
    sub = Subcategory.objects.get(id=pk)
    sub.delete()
    return redirect('index')


def update_region(request, pk):
  region = Region.objects.get(id=pk)
  if request.method == 'POST':
      name = request.POST.get('name')
  region.save(name=name)
  return redirect('index')


def update_sub(request, pk):
  sub = Subcategory.objects.get(id=pk)
  if request.method == 'POST':
      name = request.POST.get('name')
      category = request.POST.get('category')
  sub.save(name=name, category_id=category)
  return redirect('index')


def up_info(request, pk):
  info = Information.objects.get(id=pk)
  if request.method == 'POST':
      name = request.POST.get('name')
      logo = request.FILES.get("logo")
      description = request.POST.get('description')
      google = request.POST.get('google')
      apple = request.POST.get('apple')
  info.save(company_name=name, logo=logo, description=description, googleplay=google, appstore=apple)
  return redirect('index')


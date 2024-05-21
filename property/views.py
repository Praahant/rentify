from django.shortcuts import render, redirect, get_object_or_404
from .models import Property
from .forms import PropertyForm
from authentication.models import User
from django.contrib.auth.decorators import login_required

@login_required
def property_seller_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    owner = User.objects.get(pk=property.owner.pk)
    return render(request, 'property/property_seller_detail.html', {'owner': owner, 'property': property})

def property_list(request):
    properties = Property.objects.all()
    return render(request, 'property/property_list.html', {'properties': properties})

@login_required
def property_create(request):
    if request.method == 'POST':
        owner = request.user
        place = request.POST.get('place')
        area = request.POST.get('area')
        location = request.POST.get('location')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        hospitals_nearby = request.POST.get('hospitals_nearby') == "True"
        colleges_nearby = request.POST.get('colleges_nearby') == "True"
        
        propertie = Property(
            owner = owner,
            place=place,
            area=area,
            location=location,
            bedrooms=bedrooms,
            bathrooms=bathrooms,
            hospitals_nearby=hospitals_nearby,
            colleges_nearby=colleges_nearby,
        )
        propertie.save()
        return redirect('property_list')
    return render(request, 'property/property_create.html')

def property_update(request, pk):
    property = get_object_or_404(Property, pk=pk, owner=request.user)
    if request.method == 'POST':
        place = request.POST.get('place')
        area = request.POST.get('area')
        location = request.POST.get('location')
        bedrooms = request.POST.get('bedrooms')
        bathrooms = request.POST.get('bathrooms')
        hospitals_nearby = request.POST.get('hospitals_nearby') == "True"
        colleges_nearby = request.POST.get('colleges_nearby') == "True"
        
        property.place = place
        property.area = area
        property.location = location
        property.bedrooms = bedrooms
        property.bathrooms = bathrooms
        property.hospitals_nearby = hospitals_nearby
        property.colleges_nearby = colleges_nearby
        
        property.save()
        return redirect('property_list')
    return render(request, 'property/property_create.html', {'property': property})

def property_delete(request, pk):
    property = get_object_or_404(Property, pk=pk, owner=request.user)
    property.delete()
    return redirect('property_list')

def property_owned(request):
    prop = Property.objects.filter(owner=request.user)
    return render(request, 'property/property_owned.html', {'property': prop})
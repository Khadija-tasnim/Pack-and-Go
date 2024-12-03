from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import TourDestinations, TourImage
from .forms import TourDestinationForm, TourImageForm


def create_tour(request):
    if request.method == 'POST':
        form = TourDestinationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tour_list')
    else:
        form = TourDestinationForm()
    return render(request, 'tour/create_tour.html', {'form': form})


def tour_list(request):
    tours = TourDestinations.objects.all()
    return render(request, 'tour/tour_list.html', {'tours': tours})


from django.shortcuts import render, get_object_or_404, redirect
from .models import TourDestinations, TourImage
from .forms import TourImageForm


def tour_detail(request, pk):
    tour = get_object_or_404(TourDestinations, pk=pk)

    if request.method == 'POST':
        form = TourImageForm(request.POST, request.FILES)
        if form.is_valid():

            image = form.save(commit=False)
            image.tour = tour
            image.save()

            return redirect('tour_detail', pk=tour.pk)
    else:
        form = TourImageForm()

    return render(request, 'tour/tour_detail.html', {'tour': tour, 'form': form})


def update_tour(request, pk):
    tour = get_object_or_404(TourDestinations, pk=pk)
    if request.method == 'POST':
        form = TourDestinationForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            return redirect('tour/tour_detail', pk=tour.pk)
    else:
        form = TourDestinationForm(instance=tour)
    return render(request, 'tour/update_tour.html', {'form': form})


def delete_tour(request, pk):
    tour = get_object_or_404(TourDestinations, pk=pk)
    if request.method == 'POST':
        tour.delete()
        return redirect('tour/tour_list')
    return render(request, 'tour/delete_tour.html', {'tour': tour})

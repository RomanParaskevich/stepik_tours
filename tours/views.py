from django.shortcuts import render


def MainView(request):

    return render(request, 'index.html')


def DepartureView(request, departure):

    return render(request, 'departure.html')


def TourView(request, id):

    return render(request, 'tour.html')

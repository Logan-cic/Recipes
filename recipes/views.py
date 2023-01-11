from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Logan Cardoso'
    })  # recipes é um namespece

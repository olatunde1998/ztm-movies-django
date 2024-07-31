from django.shortcuts import render, HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse("My Favorite Movies")
# Sample one 
# def index(request):
#     return render(request, 'movies/index.html', {'movie' : 'gladiator'})

# Sample two  
def index(request):
    context = {
        'movies': ['gladiator', 'top gun', 'Casino']
    }
    return render(request, 'movies/index.html', context)

def about(request):
    return render(request, 'movies/about.html', {})

# app/templates/app/index.html
# movies/templates/movies/index.html
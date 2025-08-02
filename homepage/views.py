from django.shortcuts import render

from news.models import News


# Create your views here.
def homepage(request):
    crime = News.objects.filter(category__name='Crime')
    context = {
        'crime': crime,
    }
    return render(request, 'index.html', context)

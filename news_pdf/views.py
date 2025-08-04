from django.shortcuts import render
from .models import NewsPDF


# Create your views here.
def news_pdf(request):
    latest_pdf = NewsPDF.objects.last()
    print(latest_pdf.pdf_file, '==========================latest_pdf')
    return render(request, 'news_pdf.html', {'pdf': latest_pdf})

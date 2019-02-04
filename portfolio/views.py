from django.shortcuts import render
from .models import Project

# Create your views here.
def portfolio(request):
    # objects selo se crea una vez que se ejecuta
    projects = Project.objects.all()
    return render(request, "portfolio/portfolio.html",{'projects':projects})
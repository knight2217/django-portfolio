from django.shortcuts import render
from hobby.models import Hobby

# Create your views here.
def hobby_index(request):
    hobby = Hobby.objects.all()
    context = {
        'hobby': hobby
    }
    return render(request, 'hobby_index.html', context)

def hobby_detail(request, pk):
    hobby = Hobby.objects.get(pk=pk)
    context = {
        'hobby': hobby
    }
    return render(request, 'hobby_detail.html', context)
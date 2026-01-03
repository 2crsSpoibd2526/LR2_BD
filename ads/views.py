from django.shortcuts import render, redirect
from .models import Bb
from .forms import BbForm

def index(request):
    bbs = Bb.objects.all()
    return render(request, 'ads/index.html', {'bbs': bbs})

def add(request):
    if request.method == 'POST':
        form = BbForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BbForm()
    return render(request, 'ads/add.html', {'form': form})

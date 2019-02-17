from django.shortcuts import render ,redirect
from .models import Diary

# Create your views here.
def home(request):
    diarys = Diary.objects.all().order_by('-id')
    return render(request, 'home.html',{'diarys':diarys})

def create(request):
    diary = Diary()
    diary.title = request.POST['title']
    diary.description = request.POST['body']
    diary.file = request.FILES['file']
    diary.save()
    return redirect('home')
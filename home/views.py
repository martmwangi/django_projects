from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.
def index(request):
    form = StudentForm()
    context = {
        "hello_message":"Hello Moringa",
        "form": form

    }
    return render(request,'index.html', context)
    return HttpResponse("Success")

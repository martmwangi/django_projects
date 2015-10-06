from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm

# Create your views here.
def index(request):
    form = StudentForm(request.POST or None)
    context = {
        "hello_message":"Register new Student",
        "form": form

    }

    if form.is_valid():
        form.save()
        context = {
            "hello_message": "Student Saved"

        }
    print (request.POST)

    return render(request,'index.html', context)
    return HttpResponse("Success")

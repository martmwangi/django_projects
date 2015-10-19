from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .forms import FeedbackForm
from .models import Student
from django.core.mail import send_mail


# Create your views here.
def index(request):
    context = {}
    return render(request, 'home.html', context)


def register(request):
    form = StudentForm(request.POST or None)
    context = {
        "hello_message": "Register new Student",
        "form": form

    }

    if form.is_valid():
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')
        if full_name == "Jacob":
            full_name = "Developer"
        instance.full_name = full_name
        instance.save()

        context = {
            "hello_message": "Student Saved"

        }
    print (request.POST)
    return render(request, 'index.html', context)
    return HttpResponse("Success")


def feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        from_email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message = form.cleaned_data.get('message')
        prepared_message = "You have feedback {} saying '{}'".format
        ('full_name', 'message')

        # send_mail('New Feedback Given', prepared_message, from_email
        #          ['martmwangi86@gmail.com'], fail_silently=False)

        send_mail('New Feedback Given', prepared_message, from_email,
                  ['martmwangi86@gmail.com'], fail_silently=False)

    context = {
        "form": form
    }
    return render(request, 'feedback.html', context)


def students(request):
    search_term = request.GET.get('search', default='')
    students = Student.objects.all().filter(full_name__contains=search_term)
    context = {'students': students}
    return render(request, 'students.html', context)

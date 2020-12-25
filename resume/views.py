from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def resume_template(request):
#     return render(request,'resume.html')

def resume_template(request):
    return render(request ,'resume.html')
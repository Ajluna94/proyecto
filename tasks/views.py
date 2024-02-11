from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm 


# Create your views here.
def singup(request):
  return render(request,'singup.html',{
    "from": UserCreationForm
  })

  
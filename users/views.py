from django.shortcuts import render
from django.contrib.auth import login
from django.urls import reverse
from users.forms import CustomCreationForm


def dashboard(request):
    return render(request, "users/dashboard.html")


def register(request):
    if request.method == "GET":
        return render(request, "users/register.html", {"form": CustomCreationForm})
    elif request.method == "POST":
        form = CustomCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(register, user)
            return render(reverse("dashboard"))

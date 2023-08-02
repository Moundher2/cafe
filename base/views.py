from django.shortcuts import render, redirect
from .forms import BuyerForm

# Create your views here.


def home(request):
    return render(request, 'index.html')


def buy(request):
    form = BuyerForm()

    if request.method == "POST":
        form = BuyerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form": form}
    return render(request, "buy_form.html", context)

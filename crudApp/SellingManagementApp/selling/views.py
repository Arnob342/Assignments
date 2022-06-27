from django.shortcuts import render
from django.shortcuts import redirect
from selling.forms import SellingForm
from selling.models import Selling

# Create your views here.

def createSelling(request):
    if request.method == "POST":
        form = SellingForm(request.POST)
        if form.is_valid():

            form.save()
            return redirect("/show")
            pass
    else:
        form =SellingForm()

    return render(request,"index.html",{'form': form})

def show(request):
    selling = Selling.objects.all()
    return render(request, "show.html",{"selling": selling})

def edit(request, id):
    selling = Selling.objects.get(id=id)
    return render(request, "edit.html", {"selling": selling})

def update(request, id):
    selling = Selling.objects.get(id=id)
    form = SellingForm(request.POST, instance=selling)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, "edit.html", {"selling": selling})

def delete(request, id):
    selling = Selling.objects.get(id=id)
    selling.delete()
    return redirect('/show')


from django.shortcuts import render, redirect
from .models import owasp
from .forms import VulForms

TEMPLATE_DIRS = ('os.path.join(BASE_DIR, "templates")')

#fazer uma lógica CRUD 

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        form = VulForms(request.POST or None)
        form.save()
        return redirect(thankyoupage)
    return render(request,'create.html')

def thankyoupage(request):
    return render(request,'thankyou.html')

def view(request):
    vulnerabilities = owasp.objects.all().order_by('code','-year')
    return render(request,'view.html',{'dataBase':vulnerabilities})

def update(request, pk):
    items = owasp.objects.get(id=pk)

    if request.method == "POST":
        form = VulForms(request.POST, instance=items)
        form.save()
        return redirect(thankyoupage)
    return render(request,'create.html',{'forms':items})

def deleteItem(request, pk):
    item = owasp.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect(view)
    return render(request, 'delete.html',{'forms':item})
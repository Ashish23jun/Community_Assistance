from django.shortcuts import render
from datetime import datetime
from knowledge_hub.models import Query
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "index.html")

def query(request):
    if request.method=="POST":
        Email=request.POST.get("Email")
        Name=request.POST.get("Name")
        Address=request.POST.get("Address")
        City=request.POST.get("City")
        State=request.POST.get("State")
        Zip=request.POST.get("Zip")
        Comments=request.POST.get("Comments")
        query=Query(Email=Email, Name=Name, Address=Address, City=City, State=State, Zip=Zip, Comments=Comments, Date=datetime.today())
        query.save()
        messages.success(request, " The query has been sent successfully.")
    return render(request, "query.html")

def ngo(request):
    return render(request, "ngo.html")
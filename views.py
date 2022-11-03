#from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Ganesh2
# Create your views here.
def abhi(request):

    if request.method == 'POST':

        name = request.POST.get("name")

        address = request.POST.get("address")

        empID = request.POST.get("empID")

        staffid = request.POST.get("staffid")

        a = Ganesh2(name,address,empID,staffid)

        a.save()

        print(name)

        print(address)

        print(empID)

        print(staffid)

    else:

        return render(request,"data.html",context={})

    return HttpResponse("printed on Console, please Check!!")
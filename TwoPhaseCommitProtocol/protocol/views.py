from django.shortcuts import render, redirect
from .models import Site, Status
# Create your views here.
from django.http import JsonResponse
from .serializer import site_to_dict, sites_to_dict
status = ["Not Running","Prepare","Ready","Commit","Abort","Terminated"]
import requests as req

def view_all(request):
    site = Site.objects.all()
    image_detail = []

    for image in site:
        image_detail.append({
            "name": image.name,
        })
    return JsonResponse({"msg": image_detail},status=200)

def create(request,name,port):
    site = Site()
    site.name = name
    site.port = port
    site.amount = 100
    site.save()
    status = Status()
    status.site = site 
    status.status = 0
    status.save()
    return JsonResponse({"Created": site.name}, status=200)

def delete(request):
    site = Site.objects.filter(name="Site C")
    for i in site:
        i.delete()
    return JsonResponse({"message": "done"}, status=200)

def ping(request,port):
    is_site = req.get('http://localhost:8000/prepare/' + str(port))
    print(is_site.status_code)
    return JsonResponse({"message": "done"}, status=200)
        

def master_home(request):
    global status
    status_list = {}
    sites = Site.objects.all()
    for i in sites:
        status_list[i.name] = status[i.status.status]
    # sites = sites_to_dict(sites)
    return render(request,"master_home.html",{'sites': sites,'status':status})   

def reset(request):
    site = Site.objects.all()
    for i in site:
        status = Status.objects.get(site=i)
        status.status = 0
        status.save()
    return redirect('master_home')

def prepare(request,port):
    port = int(port)
    site = Site.objects.get(port=port)
    status = Status.objects.get(site=site)
    status.status = 1
    status.save()
    site = site_to_dict(site)
    return JsonResponse({"site": site},status=200)

def sendPrepare(request):
    global status
    site = Site.objects.all()
    sites = []
    non_sites = []
    for i in site:
        try:
            is_site = req.get('http://localhost:'+str(i.port)+'/protocol/prepare/' + str(i.port))
            print(i.port, is_site.status_code)
            if is_site.status_code == 200:
                sites.append(i)
            else:
                non_sites.append(i)
        except:
            non_sites.append(i)
    return render(request,"master_home.html",{'sites': sites,'non_sites':non_sites,'status':status})

def ready(request,port):
    port = int(port)
    site = Site.objects.get(port=port)
    status = Status.objects.get(site=site)
    status.status = 2
    status.save()
    site = site_to_dict(site)
    return JsonResponse({"site": site},status=200)



def sendReady(request):
    global status
    site = Site.objects.all()
    sites = []
    non_sites = []
    for i in site:
        try:
            is_site = req.get('http://localhost:'+str(i.port)+'/protocol/ready/' + str(i.port))
            print(i.port, is_site.status_code)
            if is_site.status_code == 200:
                sites.append(i)
            else:
                non_sites.append(i)
        except:
            non_sites.append(i)
    return render(request,"master_home.html",{'sites': sites,'non_sites':non_sites,'status':status})
    
def commit(request,port):
    port = int(port)
    site = Site.objects.get(port=port)
    if port == 8000:
        site.amount = 400
    else:
        site.amount = 100
    status = Status.objects.get(site=site)
    status.status = 3
    status.save()
    site = site_to_dict(site)
    return JsonResponse({"site": site},status=200)


def sendCommit(request):
    global status
    site = Site.objects.all()
    sites = []
    non_sites = []
    for i in site:
        try:
            is_site = req.get('http://localhost:'+str(i.port)+'/protocol/commit/' + str(i.port))
            print(i.port, is_site.status_code)
            if is_site.status_code == 200:
                sites.append(i)
            else:
                non_sites.append(i)
        except:
            non_sites.append(i)
    return render(request,"master_home.html",{'sites': sites,'non_sites':non_sites,'status':status})
    
def Abort(request,port):
    port = int(port)
    site = Site.objects.get(port=port)
    if port == 8000:
        site.amount = 100
    else:
        site.amount = 200
    status = Status.objects.get(site=site)
    status.status = 4
    status.save()
    site = site_to_dict(site)
    return JsonResponse({"site": site},status=200)

def sendAbort(request):
    global status
    site = Site.objects.all()
    sites = []
    non_sites = []
    for i in site:
        try:
            is_site = req.get('http://localhost:'+str(i.port)+'/protocol/abort/' + str(i.port))
            print(i.port, is_site.status_code)
            if is_site.status_code == 200:
                sites.append(i)
            else:
                non_sites.append(i)
        except:
            non_sites.append(i)
    return render(request,"master_home.html",{'sites': sites,'non_sites':non_sites,'status':status})
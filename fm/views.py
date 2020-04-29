from django.shortcuts import render
import os
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from wsgiref.util import FileWrapper
# Create your views here.

def scanner(path="D:\\"):
    files,folders=[],[]
    for i in os.scandir(path):
        if i.is_file():
            files.append(i)
        else:
            folders.append(i)
    return {'foldersfiles':folders+files}

def index(request):
    content = scanner()
    return render(request,'fm/index.html',context=content)
def view_detail(request):
    requested_data = request.GET.get('search')
    content= scanner(requested_data)
    return render(request,'fm/index.html',context=content)
def folder_view(request):
    requested_data = request.GET.get('a')
    content= scanner(requested_data)
    return render(request,'fm/index.html',context=content)
'''
def file_response(request):
    requested_data = request.GET.get('search')
    with open(requested_data) as file:
        content = file.read()
    return HttpResponse(content)
    FileWrapper(
        response = HttpResponse(file,content_type="video/mp4")
'''
def file_response(request):
    requested_data = request.GET.get('search')
    file_location = requested_data

    try:    
        #with open(file_location, 'r') as f:
          # file_data = f.read()
        file = open(file_location,'rb')
        # sending response 
        response= FileResponse(file)
        response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.split(file_location)[1])

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

    return response
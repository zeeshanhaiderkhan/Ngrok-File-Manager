from django.shortcuts import render
import os
from django.http import HttpResponse, HttpResponseNotFound, FileResponse
from wsgiref.util import FileWrapper
<<<<<<< HEAD
from fm.structure import File
from fm.mail import SendEmail
# Create your views here.
import sys
from cv2 import VideoCapture,imwrite
import json
from smartfile import BasicClient
import ctypes

def scanner(path="/root"):
    files,folders=[],[]
    for i in os.scandir(path):
        if i.is_file():
            files.append(File(i))
        else:
            folders.append(File(i))
    return {'foldersfiles':folders+files}
def shutdown(request):
    if sys.platform == 'win32':
        user32 = ctypes.WinDLL('user32')
        user32.ExitWindowsEx(0x00000008, 0x00000000)

    else:
        #os.system('sudo shutdown now')
        #os.system('systemctl poweroff') 
        print('lol')
    return HttpResponse('<h1>Shutting Down</h1>')
    
def upload_smartfile(request):
    file_path = request.GET.get('filepath') #path
    api = BasicClient("TxHYvbTZHmxnYcpTWvFYXKwPVb1xUh","Qlw9pGFhtl0MJFiOkBBWDLco4bV0yX")
    file = open(file_path,'rb')
    api.upload(os.path.split(file_path)[1],file)
    return HttpResponse("<h1>UPLOADED</h1>")

def screenshot(request):
    if sys.platform == 'linux': #differs for linux
        import pyscreenshot as ImgGrb
        ImgGrb.grab_to_file('Screenshot.png')
    else:
        from PIL import ImageGrab
        ImageGrab.grab().save("Screenshot.png")
    screenshot=open('Screenshot.png','rb')
    response= FileResponse(screenshot)
    response['Content-Disposition'] = 'attachment; filename=screenshot.png'
    return response

def settings(request):
    with open("/root/filemanager/filemanager/fm/settings.json") as settings_json:
        settings = json.load(settings_json)
    return render(request,'fm/settings.html',context=settings)

def settings_done(request):
    settings=get_requests(request,"base_directory","folder_size","file_size","email","email_password","smartfile_api","smartfile_password","webcam","screenshot","deleting","server")
    print(settings)
    with open("/root/filemanager/filemanager/fm/settings.json",'w') as settings_json:
        json.dump(settings,settings_json)
    return render(request,'fm/settings.html',context=settings)

def get_requests(request,*args):
    json_data={}
    for i in args:
        json_data[i] = request.POST.get(i)
    return json_data

def camera(request):
    cam = VideoCapture(0)
    s, img = cam.read()
    imwrite("capture.jpg",img)
    del(cam)
    picture = open('capture.jpg','rb')
    response= FileResponse(picture)
    response['Content-Disposition'] = 'attachment; filename=picture.jpg'
    return response
    
=======
# Create your views here.

def scanner(path="D:\\"):
    files,folders=[],[]
    for i in os.scandir(path):
        if i.is_file():
            files.append(i)
        else:
            folders.append(i)
    return {'foldersfiles':folders+files}

>>>>>>> 14979eb57f97c05423aea52fa679fb9552adde4f
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
<<<<<<< HEAD
def email_view(request):
    #post get ... mail address etc
    requested_data = request.GET.get('search')
    content={'file':requested_data,
             'size':File(requested_data,path=True).size()
            }
    return render(request,'fm/email.html',context=content)
    #email_setup = SendEmail(['smtp.gmail.com', 587, 'sokratis.email@gmail.com', 'iloveyousokratis1234'])
    #email_setup.send(to_address=['zeeshanraul11@gmail.com'],attachments=["/root/filemanager/filemanager/fm/img.jpg"])
def email_done(request):
    #post get ;;;
    email, message,file= request.POST.get('email'),request.POST.get('message'),request.POST.get('file')
    print(email,message,file)
    email_setup = SendEmail(['smtp.gmail.com', 587, 'sokratis.email@gmail.com', 'iloveyousokratis1234'])
    status = email_setup.send(to_address=[email],body=message,attachments=[file])
    return render(request,'fm/email_done.html',context={'status':status})
=======
>>>>>>> 14979eb57f97c05423aea52fa679fb9552adde4f
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
<<<<<<< HEAD
=======
    file_location = requested_data
>>>>>>> 14979eb57f97c05423aea52fa679fb9552adde4f

    try:    
        #with open(file_location, 'r') as f:
          # file_data = f.read()
<<<<<<< HEAD
        file = open(requested_data,'rb')
        # sending response 
        response= FileResponse(file)
        response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.split(requested_data)[1])
=======
        file = open(file_location,'rb')
        # sending response 
        response= FileResponse(file)
        response['Content-Disposition'] = 'attachment; filename={}'.format(os.path.split(file_location)[1])
>>>>>>> 14979eb57f97c05423aea52fa679fb9552adde4f

    except IOError:
        # handle file not exist case here
        response = HttpResponseNotFound('<h1>File not exist</h1>')

<<<<<<< HEAD
    return response
def file_size(path):
    ##MB
    return os.path.getsize(path)/(1024*1024)
=======
    return response
>>>>>>> 14979eb57f97c05423aea52fa679fb9552adde4f

import base64
import os
import random
import json
from flask import Flask, jsonify, current_app
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Letter

def index(request):
    images = list(Letter.objects.all())
    randomLetters = images
    sizeOfImages = len(images)
    if sizeOfImages > 20:
        randomLetters = random.sample(images, 20)
    context ={
        'images' : images,
        'randomLetters' : randomLetters,
        'sizeOfImages': sizeOfImages
    }
    
    filelist()
    
    return render(request, "main.html", context)

@csrf_exempt
def canvasToImage(request):
    data = request.POST.__getitem__('data')
    data = data[22:]
    number = random.randrange(1,1000)

    # 저장할 경로 및 파일명을 지정
    path = str(os.path.join(settings.MEDIA_ROOT, 'img/'))
    filename = 'letter' + str(number) + ".png"

    #"wb" (바이너리 파일 쓰기 전용)으로 file open
    image = open(path+filename, "wb")
    # 'base64.b64decode()'를 통하여 디코딩 하고 파일을 쓴다.
    image.write(base64.b64decode(data))
    image.close()

    uploadImage(filename, "img/"+filename)

    return render(request, "main.html")

def uploadImage(filename, image):
    form = Letter()
    form.title = filename
    form.image = image
    form.save()
    
@staticmethod
def filelist():
    app = Flask(__name__)
    with app.app_context():
        cwd = os.getcwd() #현재 path
        
        print(os.listdir(cwd + '/media/img'))
        list = os.listdir(cwd + '/media/img')
        response={
            "response" : list
        }
        
        json_return=json.dumps(response)   #string #json
        print("json_return", json_return)
        return jsonify(response)
import base64
import json
import os
import random
from urllib import request
from django.shortcuts import render
from letterOnTree import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    return render(request, "testLetterCreate.html")

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

    answer ={
        'title': filename,
        'image': path
    }
    letters = []
    letter = {}
    letter["model"] = "letterOnTreeApp.Letter"
    letter["fields"] = {}
    
    for key, value in answer.items():
        if key in ['title', 'image']:
            letter["fields"][key] = value
        letters.append(letter)

    with open('letters.json', 'w', encoding="utf-8") as make_file: 
            json.dump(letters, make_file, ensure_ascii=False, indent="\t") 
    return render(request, "testLetterCreate.html")

    
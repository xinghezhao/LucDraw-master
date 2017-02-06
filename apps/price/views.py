# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.http import HttpResponse #指定返回给用户的类型

from .models import UserMessage
from .forms import UploadImageForm
import json


# Create your views here.

def getform(request):

    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')

        user_message = UserMessage()
        user_message.name = name
        user_message.email = email
        user_message.message = message
        user_message.address = address
        #保存图片到数据库并且到相应文件夹
        image_form = UploadImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            headImg = image_form.cleaned_data['image']
            user_message.image = headImg
        user_message.save()


    return render(request, 'message-form.html',{})




def edit_favorites(request):
    if request.is_ajax():
        aList = []
        if request.method == 'GET':
            message = "Yes, AJAX is get!"
        elif request.method == 'POST':
            headphotos = UserMessage.objects.all()
            for headphoto in headphotos:
                try:
                    aList.append(headphoto.image.url)
                    print aList
                except:
                    continue
    else:
        message = "Not Ajax"
    return HttpResponse(json.dumps(aList), content_type="application/json")




def favorites(request):

    return render(request,'index.html',{})







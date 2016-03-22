from django.shortcuts import render

from .models import UserInfo,DiscussionTopic
from .forms import PostTopic

# Create your views here.
def index(request):
    print (request.method)
    return render(request,'index.html')

def register(request):
    print request.method
    if request.method == 'GET':
        return render(request,'register.html')
   # print request.POST['fname']
    new_user = UserInfo(fname = request.POST['fname'])
    new_user.save()
    return render(request,'index.html')

def postTopic(request):
    form  = PostTopic()
    return render(request,'postTopic.html',{'form':form})

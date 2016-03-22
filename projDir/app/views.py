from django.shortcuts import render

from .models import UserInfo,DiscussionTopic
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
    topics = DiscussionTopic.objects.all()
    return render(request,'postTopic.html',{'topics':topics})


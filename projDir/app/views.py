from django.shortcuts import render,redirect

from .models import UserInfo,DiscussionTopic
from .forms import PostTopic,RegisterUser

from django.contrib.auth.hashers import make_password

# Create your views here.
def index(request):
    print (request.method)
    return render(request,'index.html',{'form':form})

#view for registering the user
def register(request):
    if request.method == 'POST':
        form  = RegisterUser(request.POST)
        #print form
        #creating an instance of new topic
        if form.is_valid():
            post = form.save(commit=False) #false means that do not save the instance
            post.fname = request.POST['fname']
            post.lname = request.POST['lname']
            post.username = request.POST['username']
            post.password = make_password(password=request.POST['password'],
                                  salt=None,
                                  hasher='unsalted_md5')
            post.save()
            return redirect('index');
    else:
        form = RegisterUser()
    return render(request,'registerUser.html',{'form':form})


def postTopic(request):
    form  = PostTopic()
    return render(request,'postTopic.html',{'form':form})

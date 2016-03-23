from django.shortcuts import render,redirect
from .models import UserInfo,DiscussionTopic,CommentOfTopic
from .forms import PostTopic,RegisterUser,PostComment
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.utils import timezone
import md5
import datetime



# Create your views here.
def index(request):
    return render(request,'index.html')



def login(request):
    #print (request.method)
    if request.method == 'POST':
        inputUsername = request.POST['username']
        inputPassword = request.POST['password']
        try:
            user = UserInfo.objects.get(username = inputUsername)
            inputHashedPassword = md5.new(inputPassword).hexdigest()
            if inputHashedPassword == user.password:
                user.is_authenticated = True
                request.user = user
                request.user.username = user.username
                request.session['uid'] = user.id
                request.session['username'] = user.username
                return redirect('postTopic');
            else:
                return HttpResponse('Username and Password mismatch')
        except:
            return HttpResponse('No such User');
    return render(request,'login.html')



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
            post.password = md5.new(request.POST['password']).hexdigest()
            post.save()
            return redirect('login')
    else:
        form = RegisterUser()
    return render(request,'registerUser.html',{'form':form})


def login_required(func):
    def wrapper(request,*args,**kwargs):
        #print request.session['uid']
        if 'uid' not in request.session.keys():
            return redirect('login')
        return func(request,*args,**kwargs)
    return wrapper

@login_required
def postTopic(request):
    if request.method == 'POST':
        form = PostTopic(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            user = UserInfo.objects.get(username = request.session['username'])
            post.user = user
            post.topicText = request.POST['topicText']
            post.timeStamp = datetime.datetime.now() #change the time according to country
            post.save()
            return redirect('postTopic')
    else:
        form  = PostTopic()
        topics = DiscussionTopic.objects.all()
    return render(request,'postTopic.html',{'form':form,'topics':topics})


@login_required
def topicDetails(request,id):
    topic = DiscussionTopic.objects.get(id = id)
    form = PostComment()
    try:
        comments = CommentOfTopic.objects.all()
    except:
        return render(request,'topicDetails.html',{'form':form,'topic':topic})
    return render(request,'topicDetails.html',{'form':form,'topic':topic,'comments':comments})

@login_required
def postComment(request,id):
    if request.method == 'POST':
        form  = PostComment(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.topic = DiscussionTopic.objects.get(id = id)  #instance of topic with id
            post.user = UserInfo.objects.get(username = request.session['username'])  #instance of the user
            post.commentText = request.POST['commentText']
            post.timeStamp = datetime.datetime.now()
            post.save()
            return redirect('/topicDetails/'+id)
    return redirect('/topicDetails/'+id)

def logout(request):
    del request.session['uid']
    return redirect('index')

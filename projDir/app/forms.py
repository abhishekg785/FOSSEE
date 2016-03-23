from django import forms
from .models import DiscussionTopic,UserInfo

#postTopic is the name of my form
class PostTopic(forms.ModelForm):
    class Meta:
        model = DiscussionTopic
        fields = ('topicText',)


class RegisterUser(forms.ModelForm):
    fname = forms.CharField(label = 'First Name:')
    lname = forms.CharField(label = 'Last Name:')
    password = forms.CharField(widget=forms.PasswordInput,label='Password')
    class Meta:
        model = UserInfo
        fields = ('fname','lname','username','password')

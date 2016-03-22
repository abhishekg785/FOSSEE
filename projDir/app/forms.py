from django import forms
from .models import DiscussionTopic,UserInfo

#postTopic is the name of my form
class PostTopic(forms.ModelForm):


    class Meta:
        model = DiscussionTopic
        fields = ('topicText',)


class RegisterUser(forms.ModelForm):

    class Meta:
        model = UserInfo
        fields = ('fname','lname','username','password')

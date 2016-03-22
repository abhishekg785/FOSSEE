from django import forms
from .models import DiscussionTopic

#postTopic is the name of my form
class PostTopic(forms.ModelForm):


    class Meta:
        model = DiscussionTopic
        fields = ('topicText',)

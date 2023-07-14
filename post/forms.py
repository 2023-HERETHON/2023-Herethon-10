from django import forms
from .models import JarPost, CounselPost, CounselComment, CounselRecomment

class CounselPostForm(forms.ModelForm):
    class Meta:
        model = CounselPost
        fields = ['title', 'content', 'hashtag', 'image']
        # widgets = {
        #     'title' : forms.TextInput(attrs={'class':'a',})
        # }

class CounselCommentForm(forms.ModelForm):
    class Meta:
        model = CounselComment
        fields = ['comment']

class CounselRecommentForm(forms.ModelForm):
    class Meta:
        model = CounselRecomment
        fields = ['recomment', 'comment']

class JarPostForm(forms.ModelForm):
    class Meta:
        model = JarPost
        fields = ['content', 'image']




from django import forms
from . import models

class CreateArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'slug', 'thumb']

class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ['body']

class EditArticleForm(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'body', 'thumb']
    
    def setValues(self, title, body, thumb):
        self.title = title
        self.body = body
        self.thumb = thumb
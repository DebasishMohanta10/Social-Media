from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields["text"].widget.attrs["class"] = "block p-2.5 w-full text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        self.fields["text"].widget.attrs["rows"] =3
        self.fields["text"].label = "Comment"
    class Meta:
        model = Comment
        fields = ['text']
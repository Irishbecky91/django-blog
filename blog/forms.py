from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """
    This class tells the comment form what model to use and which 
    fields to display the forms in.
    """
    class Meta:
        """
        Meta class
        """
        model = Comment
        fields = ('body',)

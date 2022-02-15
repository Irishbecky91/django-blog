"""
This is the admin.py page
"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post


# Register your models here.
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Class will use summernote for blog content
    """
    summernote_fields = ('content')

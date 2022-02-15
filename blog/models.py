"""
This is the models.py page
"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))


class Post(models.Model):
    """
    This class defines the Post features
    """
    title = models.CharField(max_length=200, unique=True)
    # Title section of Entity Relationship Diagram
    slug = models.SlugField(max_length=200, unique=True)
    # Slug section of Entity Relationship Diagram
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='blog_posts'
        )
    # Author section of Entity Relationship Diagram
    updated_on = models.DateTimeField(auto_now=True)
    # Updated Date section of Entity Relationship Diagram
    content = models.TextField()
    # Content section of Entity Relationship Diagram
    featured_image = CloudinaryField('image', default='placeholder')
    # Featured Image section of Entity Relationship Diagram
    excerpt = models.TextField(blank=True)
    # Excerpt section of Entity Relationship Diagram
    created_on = models.DateTimeField(auto_now_add=True)
    # Created Date section of Entity Relationship Diagram
    status = models.IntegerField(choices=STATUS, default=0)
    # Status section of Entity Relationship Diagram
    likes = models.ManyToManyField(
        User,
        related_name='blogpost_likes',
        blank=True
        )
    # Likes section of Entity Relationship Diagram

    class Meta:
        """
        Ordering our posts in created order, the '-' means in decending order.
        """
        ordering = ['-created_on']

    def __str__(self):
        """
        Returns string representation of the object
        """
        return self.title

    def number_of_likes(self):
        """
        Returns the total number of likes on a post
        """
        return self.likes.count()


class Comment(models.Model):
    """
    This class defines the Post features
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments'
        )
    # Post section of Comment Diagram
    name = models.CharField(max_length=80)
    # Name section of Comment Diagram
    email = models.EmailField()
    # Email section of Comment Diagram
    body = models.TextField()
    # Body section of Comment Diagram
    created_on = models.DateTimeField(auto_now_add=True)
    # Created On section of Comment Diagram
    approved = models.BooleanField(default=False)
    # Approved section of Comment Diagram

    class Meta:
        """
        Ordering our posts in created order,
        the lack of '-' means in ascending order.
        """
        ordering = ['created_on']

    def __str__(self):
        """
        Returns a string showing the author's name and content of the comment.
        """
        return f"Comment {self.body} by {self.name}"

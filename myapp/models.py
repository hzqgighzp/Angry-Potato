from django.db import models
from custom_user.models import UserProfile


class ClassifyModel(models.Model):
    name = models.CharField(null=False, max_length=512, verbose_name = "Category", unique=True)
    class Meta:
        verbose_name = "Categories"
        verbose_name_plural = verbose_name
    
    def save(self, *args, **kwargs):
        if self.name == '':
            self.name = 'Unnamed'
            super(ClassifyModel, self).save(*args, **kwargs)
        else:
            super(ClassifyModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# Create your models here.
class MovieModel(models.Model):
    name = models.CharField(max_length=128, verbose_name = "Title")
    detail = models.TextField(null=True, default="", verbose_name = "Introduction")
    pic = models.ImageField(upload_to = "image", verbose_name = "Picture")
    actor = models.CharField(max_length = 512, verbose_name = "Actors")
    duration = models.IntegerField(verbose_name = "Duration")
    star = models.IntegerField(verbose_name = "Rating Level")
    publish_time = models.DateTimeField(verbose_name = "Release Date")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name = "Update Data")
    classify = models.ForeignKey(ClassifyModel, related_name="classify", verbose_name = "Category")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = verbose_name


# Comment form
class CommentModel(models.Model):
    '''
    One movie can have many comments.
    '''
    person = models.ForeignKey(UserProfile, unique=False, verbose_name="User")
    content = models.TextField(null=True, default="", verbose_name = "Comment")
    score = models.IntegerField(verbose_name = "Rating")
    # time when commenting
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Commenting time")
    movie = models.ForeignKey(MovieModel, related_name="tie_comment", verbose_name = "Movie")

    class Meta:
        verbose_name = "Comment"
        ordering = ['-create_time']
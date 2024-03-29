from re import T
from django.db import models
import uuid
from django.db.models.fields import NullBooleanField
from users.models import Profile

class Project(models.Model):

    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(
        null=True, blank=True, default="default_dude.png")

    # useful_links = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)

    tags = models.ManyToManyField('Tag', blank=True)
    links = models.ManyToManyField('Link', blank=True)

    created = models.DateTimeField(auto_now_add=True)
    #modified = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.title
       

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return str(self.created)

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                            primary_key=True, editable=False)

    def __str__(self):
        return self.name
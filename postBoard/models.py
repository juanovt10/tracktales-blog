from django.db import models
from djnago.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_lenght=200, uniquie=True)
    slug = models.SlugField(max_lenght=200, uniquie=True)
    type_tags = models.ManyToManyField(Tag) 
    author = ForeignKey(User, in_delete=models.CASCADE, related_name="board_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    public = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]
        return self.title

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = ForeignKey(User, in_delete=models.CASCADE, related_name="post_comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta: 
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    
WOLRD_AREAS = [
    ("north_america", "North America"),
    ("south_america", "South America"),
    ("europe", "Europe"),
    ("south_asia", "South Asia"), 
    ("east_asia", "East Asia"),
    ("weat_asia", "West Asia"),
    ("oceania", "Oceania"),
    ("africa", "Africa")
    ("middle_east", "Middle East"),
]

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    username = ForeignKey(User, in_delete=models.CASCADE, related_name="post_comments")
    display_name = models.TextField()
    user_description = models.TextField()
    most_visited_area = models.CharField(max_length=50, choices=WOLRD_AREAS)
    languages = models.TextField(blank=True, null=True)
    countries_traveled = models.IntegerField(default=1)
    sign on = models.BooleanField(default=False)
    approved = models.BooleanField(default=False)

    def get_tags_count(self):
        return Tag.objects.filter(post__in=self.post_set.all()).distinct().count()

    def __str__(self):
        return self.user_name


    

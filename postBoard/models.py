from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

WORLD_AREAS = [
    ('', 'Wolrd Area'),
    ("north_america", "North America"),
    ("south_america", "South America"),
    ("europe", "Europe"),
    ("south_asia", "South Asia"), 
    ("east_asia", "East Asia"),
    ("west_asia", "West Asia"),
    ("oceania", "Oceania"),
    ("africa", "Africa"),
    ("middle_east", "Middle East"),
]

TAGS = [
    ('', 'Holiday Type'),
    ("nightlife", "Nightlife"),
    ("sightseeing", "Sightseeing"),
    ("gastronomy", "Gastronomy"),
    ("culture", "Culture"),
    ("shopping", "Shopping"),
    ("relaxation", "Relaxation"),
    ("history", "History"),
    ("adventure", "Adventure"), 
    ("accomodation", "Acoomodation"),
    ("nature", "Nature"),
    ("festivals", "Festivals"),
    ("beach", "Beach"),
]


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = models.CharField(max_length=50, choices=TAGS, default='sightseeing')
    world_area = models.CharField(max_length=50, choices=WORLD_AREAS, default='europe')
    country = models.CharField(max_length=50, default='Enter Country')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="board_posts")
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]


    def __str__(self):
        return self.title


    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_comments")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]


    def __str__(self):
        return f"Comment {self.body} by {self.author.username}"


class UserProfile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    display_name = models.TextField()
    user_description = models.TextField()
    most_visited_area = models.CharField(max_length=50, choices=WORLD_AREAS)
    languages = models.TextField(blank=True, null=True)
    countries_traveled = models.IntegerField(default=1)
    sign_on = models.BooleanField(default=False)
    created_on = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}'s Profile"

# Signal to create a user profile when a new user is saved
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(username=instance)

# Signal to save the user profile when the user is saved
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class ContactInfo(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    subject = models.CharField(max_length=50)
    message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.subject}" 
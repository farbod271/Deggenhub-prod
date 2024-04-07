from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'local'),
        (3, 'business'),
    )

    # SKILLS = (
    #     (1, 'cooking'),
    #     (2, 'cleaning'),
    #     (3, 'dog walking'),
    #     (4, 'bike repair'),

    # )
    custom_user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, blank=True, default=1)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    email = models.EmailField(blank=False, null=True)
    # skills = models.PositiveIntegerField( choices=SKILLS, null= True, blank=True, default=1)


    # Set unique related names for groups and user_permissions to avoid clashes
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        # related_name="customuser_groups",
        # related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        # related_name="customuser_user_permissions",
        # related_query_name="customuser",
    )

class Task(models.Model):
    TASK_TYPE_CHOICES = (
        (1, 'product'),
        (2, 'service'),
    )
    TASK_ECO_CHOICES = (
        (1, 'offer'),
        (2, 'demand'),
    )
    title = models.CharField(max_length=50)
    task_type = models.PositiveSmallIntegerField(choices=TASK_TYPE_CHOICES, default=1)
    task_eco = models.PositiveSmallIntegerField(choices=TASK_ECO_CHOICES, default=1)
    description = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, related_name='tasks', on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='tasks/', blank=True)
    contact_info = models.CharField(max_length=100, null=True, blank=True, default='email')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(CustomUser, related_name='events', on_delete=models.CASCADE, default=1)
    occurance = models.DateTimeField()
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    place = models.CharField(max_length=100, null=True, blank=True, default='Deggendorf')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.title


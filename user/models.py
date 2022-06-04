from django.db import models
from django.contrib.auth.models import User


class customUsers(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE,
                                null=True,
                                    # verbose_name='custom_id2',
                                    related_name="user_v2")
    
    phone_number = models.TextField(max_length=11 , default='')
    dateofbirth= models.DateField()
    GENDER_CHOICES=(
        ('male', 'Male'),
        ('female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES ,default=None)
    

    def create_profile(sender, **kwargs):
        if kwargs['created']:
            custom_user=customUsers.objects.create(user=kwargs['instance'])         
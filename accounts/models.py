from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from PIL import Image

class User(AbstractUser):
    email = models.EmailField(unique=True)
    
user_model = get_user_model()
user_model.add_to_class('following',
                        models.ManyToManyField('self',
                            through="Follow",
                            related_name='followers',
                            symmetrical=False))

class Follow(models.Model):
    user_is_following = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_is_following')
    user_to_follow = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_to_follow')
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'{self.user_is_following} follows {self.user_to_follow}'

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=20,null=True,blank=True)
    dateOfBirth = models.DateField(null=True,blank=True)
    profile = models.ImageField(default='avatar.jpg',upload_to='profile')
    cover = models.ImageField(default='cover.jpg',upload_to='cover')
    bio = models.TextField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    def save(self,*args,**kwargs):
        super().save(*args,**kwargs)
        # img1 = Image.open(self.profile.path)
        # if img1.height > 300 or img1.width > 300:
        #     output_size1 = (300,300)
        #     img1.thumbnail(output_size1)
        #     img1.save(self.profile.path)
        # img2 = Image.open(self.cover.path)
        # if img2.height > 300 or img2.width > 300:
        #     output_size = (300,1300)
        #     img2.thumbnail(output_size)
        #     img2.save(self.cover.path)
    @property
    def get_profile_url(self):
        if self.profile != '':
            return self.profile.url
        else:
            return ""
    @property
    def get_cover_url(self):
        if self.cover != '':
            return self.cover.url
        else:
            return ""

def create_profile_for_new_user(sender,instance,created,**kwargs):
    if created:
        # try:
        Profile.objects.create(user=instance)
        print('profile is created')
        # except:
            # pass
    
post_save.connect(create_profile_for_new_user,sender=User)
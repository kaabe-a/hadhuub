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
    profile = models.ImageField(default='avatar.jpg')
    cover = models.ImageField(default='cover.jpg')
    bio = models.TextField(null=True,blank=True)
    
    def __str__(self) -> str:
        return self.user.username
    
    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)

    #     img = Image.open(self.cover.path)
    #     print(img.height)
    #     print(img.width)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (450, 300)
    #         print('hhhhhh')
    #         img.thumbnail(output_size)
    #         img.save(self.cover.path)
        


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



class Social(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    website = models.URLField(max_length=56,null=True,blank=True)
    facebook = models.URLField(max_length=56,null=True,blank=True)
    twitter = models.URLField(max_length=56,null=True,blank=True)
    linkedin = models.URLField(max_length=56,null=True,blank=True)
    github = models.URLField(max_length=56,null=True,blank=True)


def create_social_for_new_user(sender,instance,created,**kwargs):
    if created:
        # try:
        Social.objects.create(user=instance)
        print('Social is created')
        # except:
            # pass
    
post_save.connect(create_social_for_new_user,sender=User)
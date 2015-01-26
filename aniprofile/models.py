from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    avatar_local = models.ImageField(upload_to="avatars/",blank=True, null=True)
    blurb = models.CharField(max_length=255, blank=True)
    website_url = models.URLField(blank=True)
    website_text = models.CharField(max_length = 255, blank=True)
    steam_account = models.CharField(max_length = 30, blank = True)
    xbox_account = models.CharField(max_length = 20, blank = True)
    def __unicode__(self):
        return self.user.username
    def avatar(self):
        if self.avatar_local:
            url = self.avatar_local.url
        else:
            url = "/static/profile/no_avatar.png"
        return url
    @models.permalink
    def get_absolute_url(self):
        return ('user_view',(),{'user': self.user.pk})
    
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)


class Exec(models.Model):                                                                                                                            
    user = models.OneToOneField(User)
    position = models.CharField(max_length = 30)
    about = models.TextField()
    about_saved = models.TextField(null=True)                                                                                                        
    active = models.BooleanField(default=True)
    def name(self):
        return self.user.get_full_name()
    def __unicode__(self):
        return self.position +": " + self.user.first_name
    def save(self, **kwargs):
        self.about_saved = markdown.markdown(self.about)
        super(Exec, self).save(**kwargs)
    def get_absolute_url(self):
        return self.user.profile.get_absolute_url()

    class Meta:
        ordering = ['position'] # sort by posistion name, This means President comes 1st, as P < V


class OfficeHours(models.Model):
    DAYS=(
        (1, 'Monday'),
        (2, 'Tuesday'),
        (3, 'Wednesday'),
        (4, 'Thursday'),
        (5, 'Friday'),
    )
    start = models.TimeField()
    end = models.TimeField()
    day = models.CharField(choices=DAYS, max_length=1)
    club_exec = models.ForeignKey(Exec)

    def day_string(self):
        return str(self.DAYS[self.day-1][1])

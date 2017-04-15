from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from . import manager

class OurGroup(Group):
    """
    This was needed to have a have a display name for the groups too which admin could set according to his whims
    """
    display_name = models.CharField(_('display name'), max_length=254, blank=True, default="")
    is_deleted = models.BooleanField(default=False, blank=True)

    class Meta:
        app_label = 'userprofile'


class User(AbstractBaseUser):
    firstname=models.CharField(max_length=100,null=True,blank=False)
    lastname=models.CharField(max_length=100,null=True,blank=True)
    email=models.EmailField(blank=False, unique=True)
    username=models.CharField(max_length=100,null=True,blank=False)
    # password=models.CharField(max_length=50,null=True,blank=False)
    mobile_no=models.CharField(max_length=11,null=True,blank=False)
    college=models.CharField(max_length=11,null=True,blank=False)
    roll_no=models.CharField(max_length=11,null=True,blank=False,unique=True)
    #group=models.ManyToManyField()
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=False)
    groups = models.ManyToManyField(
        OurGroup, verbose_name=_('account groups'), blank=True, related_name="account_user_set",
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'))
    USERNAME_FIELD = 'email'
    objects = manager.CustomUserManager()

    def __unicode__(self):
        return self.email
    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        parts = [self.firstname, self.lastname]
        return " ".join(x for x in parts if x)

    def get_short_name(self):
        """
        Returns the short name for the user.
        """
        return self.firstname.strip() if self.firstname else None

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def forgot_password(self, *args, **kwargs):
        """
        send random password and link the password edit form
        """

        User.password_change(self)
        super(User, self).save(*args, **kwargs)

    def password_change(self):
        password = User.objects.make_random_password()

        #Send random generated password and link to password edit form
        # Commenting this code as SMTP server not working
        ask_for_password_change(password, self.get_full_name(), self.email)

        self.set_password(password)

    @property
    def is_superuser(self):
        return self.is_staff

    @property
    def is_admin(self):
        return self.is_staff

    def has_perm(self, perm, obj=None):
        if self.is_superuser:
            return True
        return perm in self.get_all_perm_name_label()

    def has_module_perms(self, app_label):
        return True

    def get_perms(self):
        all_perms = []
        for group in self.groups.all():
            all_perms += group.permissions.all()
        return all_perms

    def get_perms_names(self):
        all_perms = []
        for group in self.groups.all():
            for perm in group.permissions.all():
                all_perms.append(str(perm.codename))
        return all_perms

    def get_all_groups_names(self):
        all_groups = []
        for group in self.groups.all():
            all_groups.append(str(group.name))
        return all_groups

    def get_all_perm_name_label(self):
        """
        :return all permission in format <app_label>.<codename>:
        """
        all_perms = []
        for group in self.groups.all():
            for perm in group.permissions.all():
                all_perms.append(str(perm.content_type.app_label) + "." + str(perm.codename))
        return all_perms

    def save(self, *args, **kwargs):
        """ """
        self.set_password(self.password)        
        super(User, self).save(*args, **kwargs)
        
class UserPreference(models.Model):
    ZERO = '0'
    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    ROOM_SIZE = (
    (FIRST, "Single Seater"),
    (SECOND, "Double Seater"),
    (THIRD, "Triple Seater"),
    )
    ROOM_TYPE = (
    ("NON-AC", "NON-AC"),
    ("AC", "AC"),
    )
    room_size=models.CharField(max_length=15,choices=ROOM_SIZE,default=FIRST)
    room_type=models.CharField(max_length=15,choices=ROOM_TYPE,default="NON_AC")
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)

    def __unicode__(self):
        return self.user.email if self.user else self.room_type
        
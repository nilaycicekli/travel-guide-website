from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


from .models import Profile

def user_profile(sender, instance, created, **kwargs):
	if created:
        # in case we want to add user to a group
		# group = Group.objects.get(name='')
		# instance.groups.add(group)
        
		Profile.objects.create(
			user=instance,
			#email=instance.email
			)
		print('Profile created!')

post_save.connect(user_profile, sender=User)
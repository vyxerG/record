

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile
from django.contrib.auth.models import User  # built-in

# from django.core.mail import send_mail

# from django.conf import settings


# # @receiver(post_save, sender=Profile)  # This does the same thing as: post_save.connect(profileUpdated, sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    # print('Profile signal triggered!!')
    # This get fired anytime a user or a profile is created
    if created:
        # if user is created go ahead an set the instance which is the sender or Model
        user = instance
        #user=user set the current user that triggered the profile, so this automatically connects the user to the new profile.
        # Then using the  name of the the user as the profile username
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )
        # https://myaccount.google.com/lesssecureapps: This helps fix the error of gmail not being recorgnized
        # subject = 'Welcome to DevSearch'
        # message = 'We are glad you are here!'
        # send_mail(
        #     subject,
        #     message,
        #     settings.EMAIL_HOST_USER,
        #     [profile.email],
        #     fail_silently=False,
        # )
        # print('Email has been sent successfully: ')


def updateUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user
    # Assign the values based of the profile to the User while updating the profile as the profile and user has One_to_One relationship
    # leaving the created == False help it be in a condition where by the user can only update if it is not the first time of creating the profile
    if created == False:  # Can only Update it when it's not created
        # Updates the admin/User firstName with name while updating the profile
        user.first_name = profile.name
        # Updates the admin/User userName with UserName while updating the profile
        user.username = profile.username
        # Updates the admin/User email with email while updating the profile
        user.email = profile.email
        user.save()  # Then save it all for the User/admin


def deleteUser(sender, instance, **kwargs):
    user = instance.user  # This calls the present user possessing the profile that will be deleted then deletes it when the profile is being deleted, reasons is because the user has an automatic delete as OneToOneRelationship with the present user so when a particular profile is being deleleted it will not delete the profile but with the help of getting the instance of the user possessing the present or that particular profile when deleted that particular user gets deleted as well.
    user.delete()
    print('Deleting User...')


post_save.connect(createProfile, sender=User)
# The profile when triggered updates the User's values
post_save.connect(updateUser, sender=Profile)
post_delete.connect(deleteUser, sender=Profile)

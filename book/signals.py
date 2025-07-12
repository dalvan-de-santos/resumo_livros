from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Users
from rolepermissions.roles import assign_role


@receiver(post_save, sender=Users)
def definer_permissoes(sender, instance, created, **kwargs):
    if created:
        if instance.cargo == "A":
            assign_role(instance, 'adm')
        
        elif instance.cargo == "E":
            assign_role(instance, "editor")
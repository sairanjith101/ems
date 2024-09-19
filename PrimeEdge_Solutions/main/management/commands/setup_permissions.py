# your_app/management/commands/setup_permissions.py
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Setup permissions for managers'

    def handle(self, *args, **kwargs):
        # Create a new group for managers if it doesn't exist
        manager_group, created = Group.objects.get_or_create(name='Managers')
        
        # Add all permissions to the manager group
        content_types = ContentType.objects.all()
        for content_type in content_types:
            permissions = Permission.objects.filter(content_type=content_type)
            manager_group.permissions.add(*permissions)

        # Create or get the manager user
        manager_user, created = User.objects.get_or_create(username='manager', defaults={
            'password': 'password',  # Set a default password or generate one
        })
        
        # Add the manager user to the manager group
        manager_user.groups.add(manager_group)

        self.stdout.write(self.style.SUCCESS('Successfully set up manager permissions'))

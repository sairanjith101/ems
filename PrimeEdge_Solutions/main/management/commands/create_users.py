from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Employee 

class Command(BaseCommand):
    help = 'Create User accounts for existing employees'

    def handle(self, *args, **kwargs):
        employees = Employee.objects.all()
        for emp in employees:
            user, created = User.objects.get_or_create(username=emp.employee_id, email=emp.email)
            if created:
                user.set_password('initial_password')
                user.save()
                emp.user = user
                emp.save()
        self.stdout.write(self.style.SUCCESS('Successfully created or updated user accounts.'))

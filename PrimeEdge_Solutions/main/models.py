from django.db import models
from django.utils import timezone
from datetime import date
from django.contrib.auth.models import User,Group, Permission
from django.contrib.contenttypes.models import ContentType

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=False, blank=False, default='FirstName')
    last_name = models.CharField(max_length=50, null=False, blank=False, default='LastName')
    email = models.EmailField(unique=True, default='default@example.com')
    phone_number = models.CharField(max_length=15, null=False, blank=False)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, related_name='employees')
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='employees')
    date_of_birth = models.DateField(default=date.today)
    date_of_joining = models.DateField(default=date.today)
    address = models.CharField(max_length=255, default='Unknown Address')
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    employee_id = models.CharField(max_length=20, unique=True, default='00000')
    status = models.CharField(max_length=20, choices=[('Active', 'Active'), ('On Leave', 'On Leave'), ('Inactive', 'Inactive')], default='Active')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ['last_name', 'first_name']


class Attendance(models.Model):
    ATTENDANCE_STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Half Day', 'Half Day'),
        ('On Leave', 'On Leave'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=ATTENDANCE_STATUS_CHOICES, default='Absent')

    def __str__(self):
        return f'{self.employee} - {self.date} - {self.status}'

class LeaveRequest(models.Model):
    LEAVE_TYPE_CHOICES = [
        ('Sick Leave', 'Sick Leave'),
        ('Vacation', 'Vacation'),
        ('Casual Leave', 'Casual Leave'),
    ]
    
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved by TL', 'Approved by TL'),
        ('Approved by Manager', 'Approved by Manager'),
        ('Rejected', 'Rejected'),
    ]

    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    tl = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='tl_requests')
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, null=True, blank=True, related_name='manager_requests')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)
    processed_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.employee} - {self.leave_type} - {self.status}'
    

# def setup_manager_permissions():

#     manager_group, created = Group.objects.get_or_create(name='Managers')
    
#     content_types = ContentType.objects.all()
#     for content_type in content_types:
#         permissions = Permission.objects.filter(content_type=content_type)
#         manager_group.permissions.add(*permissions)

#     manager_user, created = User.objects.get_or_create(username='manager', defaults={
#         'password': 'password',
#     })
    
#     manager_user.groups.add(manager_group)
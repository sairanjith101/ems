from django.contrib import admin
from .models import Employee, Department, Attendance, LeaveRequest, Position

# Register your models here.

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Attendance)
admin.site.register(LeaveRequest)
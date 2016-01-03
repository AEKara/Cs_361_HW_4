from django.contrib.admin import site
from Design_Page.models import Course, Student, Teacher

site.register(Course)
site.register(Student)
site.register(Teacher)


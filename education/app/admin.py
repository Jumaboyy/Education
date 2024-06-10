from django.contrib import admin

# Register your models here.
from .models import Course,Teacher,Student

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','status','experience','course')
    list_display_links = ('id','full_name')
    search_fields = ('full_name',)
    list_editable = ('experience',)

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id','name','lifetime','price')
    list_display_links = ('id','name')
    search_fields = ('name',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id','full_name','phone','email','parentsphone','address','course','teacher')
    list_display_links = ('id','full_name')
    search_fields = ('full_name',)
    list_editable = ('course','teacher')
    list_filter = ('course','teacher')


admin.site.register(Course,CourseAdmin)
admin.site.register(Teacher , TeacherAdmin)
admin.site.register(Student,StudentAdmin)

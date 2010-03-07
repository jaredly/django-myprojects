from django.contrib import admin
from myprojects.models import Project, Type

class TypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Type, TypeAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'time')
    list_filter = ('types', 'status')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Project, ProjectAdmin)

# vim: et sw=4 sts=4

from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", 'phone', "name",]
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Post)
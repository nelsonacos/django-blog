from django.contrib import admin
from .models import *


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "image", "status", "created", "updated", "deleted")


class AuthorAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "created", "updated", "deleted")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)
admin.site.register(Company)
admin.site.register(SocialNetwork)
admin.site.register(Contact)
admin.site.register(Subscriber)

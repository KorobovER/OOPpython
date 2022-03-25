from django.contrib import admin
from .models import AdvUser
from .models import Posts


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'status', 'author', 'image', 'created_at')
    fields = (('author'), 'title', 'description', 'category', 'status', 'image')


admin.site.register(Posts, PostsAdmin)
admin.site.register(AdvUser)

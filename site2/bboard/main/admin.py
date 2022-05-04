from django.contrib import admin
from .forms import BbAdminForm
from .models import AdvUser, AddCommentary, AdditionalImage, Category, Posts


class AddCommentaryComInLine(admin.TabularInline):
    model = AddCommentary


class AdditionalImageInline(admin.TabularInline):
    model = AdditionalImage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'category', 'status', 'author', 'image', 'created_at')
    fields = (('author'), 'title', 'description', 'category', 'status', 'image')
    inlines = (AdditionalImageInline, AddCommentaryComInLine)
    list_filter = ('status', 'category')
    form = BbAdminForm


admin.site.register(Posts, PostsAdmin)
admin.site.register(AdvUser)
admin.site.register(AdditionalImage)
admin.site.register(Category, CategoryAdmin)

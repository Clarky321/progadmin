from django.contrib import admin
from .models import Section, Post, PostImage

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "slug")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title",)

class PostImageInline(admin.StackedInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "section", "status", "published_at")
    list_filter = ("status", "section")
    search_fields = ("title", "excerpt", "content")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [PostImageInline]
    date_hierarchy = "published_at"
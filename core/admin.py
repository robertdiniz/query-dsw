from django.contrib import admin
from .models import Author, Book, Tag, Profile, Review

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name', 'bio')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_tags')
    list_filter = ('author', 'tags')
    search_fields = ('title', 'summary', 'author__name')

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'website')
    search_fields = ('user__username', 'bio')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'rating', 'review_text')
    list_filter = ('rating', 'book')
    search_fields = ('book__title', 'review_text')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Review, ReviewAdmin)

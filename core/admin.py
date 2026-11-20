from django.contrib import admin
from .models import BlogPost, ContactMessage, NewsletterSubscriber


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email')
    readonly_fields = ('created_at',)


@admin.register(NewsletterSubscriber)
class NewsletterSubscriberAdmin(admin.ModelAdmin):
    list_display = ('email', 'subscribed_at')
    search_fields = ('email',)
    readonly_fields = ('subscribed_at',)


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'published_at', 'is_live')
    list_filter = ('status', 'category')
    search_fields = ('title', 'summary', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'published_at'
    list_editable = ('status',)
    actions = ['publish_selected', 'unpublish_selected']
    fieldsets = (
        (None, {'fields': ('title', 'summary', 'body')}),
        ('Settings', {'fields': ('category', 'cover_image', 'author_name', 'status', 'published_at', 'slug')}),
    )

    @admin.display(boolean=True, description='Visible on site')
    def is_live(self, obj):
        return obj.is_live

    @admin.action(description='Publish selected posts')
    def publish_selected(self, request, queryset):
        queryset.update(status=BlogPost.STATUS_PUBLISHED)

    @admin.action(description='Move selected posts back to draft')
    def unpublish_selected(self, request, queryset):
        queryset.update(status=BlogPost.STATUS_DRAFT)

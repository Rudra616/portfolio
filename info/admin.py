from django.contrib import admin
from .models import Message, Project, ProjectImage


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'send_time', 'is_read')
    list_filter = ('is_read', 'send_time')
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('send_time',)  # Make send_time readonly


class ProjectImageInline(admin.TabularInline):  # Or use StackedInline for bigger thumbnails
    model = ProjectImage
    extra = 3  # Show 3 empty slots for adding images
    readonly_fields = ('image_tag',)  # Optional: show thumbnail previews in admin

    # Optional: Show image preview in admin
    def image_tag(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />'
        return "-"
    image_tag.allow_tags = True
    image_tag.short_description = 'Preview'


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'github_link', 'live_link', 'icon_class', 'tag_list')
    search_fields = ('name', 'tags')
    inlines = [ProjectImageInline]  # Allow adding images directly in Project form

    # Optional: display tags as list
    def tag_list(self, obj):
        return ", ".join([tag.strip() for tag in obj.tags.split(',')])
    tag_list.short_description = 'Tags'

from django.contrib import admin
from .models import Post, Group


EMPTY_VALUE_DISPLAY = '-пусто-'


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author', 'group')
    list_editable = ('group',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = EMPTY_VALUE_DISPLAY


admin.site.register(Post, PostAdmin)


class GroupAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description',
    )
    empty_value_display = EMPTY_VALUE_DISPLAY


admin.site.register(Group, GroupAdmin)

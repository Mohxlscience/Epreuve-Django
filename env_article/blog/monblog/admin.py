from django.contrib import admin
from monblog.models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')
    search_fields = ('title', 'author__username')
    list_filter = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('title', 'content', 'author')
        }),
    )

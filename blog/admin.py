from django.contrib import admin
from .models import Post,Category,Tag
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    fields = ['title', 'body', 'excerpt', 'category', 'tags']
    
    def save_modle(self, request, obj, form, change):
        obj.author = request.user
        super().save_modle(request, obj, form ,change)
admin.site.register(Post,PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
from django.contrib import admin
from .models import Category, Video, Comment, UserProfile, View

admin.site.register(Category)
admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(View)
# Register your models here.

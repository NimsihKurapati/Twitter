from django.contrib import admin
from .models import Tweet
from .models import T_user

# Register your models here.
# admin.site.register(Tweet)

class Tweet_admin(admin.ModelAdmin):
    list_display = ('user', 'original', 'content', 'date_time','location','uuid','RT')
    search_fields = ('user',)
admin.site.register(Tweet, Tweet_admin)

class T_user_admin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email', 'user_image')
admin.site.register(T_user, T_user_admin)
from django.contrib import admin
from books.models import BookInfo, AuthorsInfo
# Register your models here.




@admin.register(BookInfo)
class BookInfoAdmin(admin.ModelAdmin):
    pass

@admin.register(AuthorsInfo)
class AuthorsInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    # actions_on_bottom = True
    list_display = ['aname', 'acomment']

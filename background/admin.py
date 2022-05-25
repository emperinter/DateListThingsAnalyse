from django.contrib import admin
from .models import User,ListThings
# Register your models here.

class ListInfo(admin.TabularInline):
    model = ListThings
    extra = 2

admin.site.unregister(User)
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = [ListInfo]

    # 展示
    list_display = ['user_id','user_name','user_passwd']
    list_filter = ['user_name']
# admin.site.register(User,UserAdmin)


admin.site.unregister(ListThings)
@admin.register(ListThings)
class ListAdmin(admin.ModelAdmin):
    # 展示
    list_display = ['things_id','userid','date','process','emotion','energy','key']
    list_filter = ['userid']
    list_per_page = 10
    search_fields = ['userid']

    # 添加、修改页属性
    fieldsets = [
            ("User",{"fields":['userid']}),
            ("ListInfo",{"fields":["date","process","emotion","energy","key"]}),
        ]
# admin.site.register(ListThings,ListAdmin)
from django.contrib import admin
from .models import Book
# Register your models here.

class BookAdmin(admin.ModelAdmin):

    def is_cheap(self):
        if self.price > 20:
            return "贵"
        else:
            return "便宜"
    is_cheap.short_description = "价格程度"
    list_display = [
        "name", "price", is_cheap
    ]
    search_fields = [
        "name", "price"
    ]
    # 指定过滤条件
    list_filter = [
        "name", 'price'
    ]
    # 指定排序的字段
    ordering = ["-price", "name"]
    #
    list_per_page = 1
    fieldsets = (
        ("基本信息", {"fields": ["name",]}),
        ("售价信息", {"fields": ("price", )})
    )

class DaDaAdminSite(admin.AdminSite):
    site_header = "达达学堂"
    site_title = "小达达"
    site_url = "http://www.baidu.com"

# admin.site.register(Book, BookAdmin)
site = DaDaAdminSite()
site.register(Book, BookAdmin)

from django.contrib import admin
from .models import Product, Brand, Address, Category

class productAdmin(admin.ModelAdmin):
    readonly_fields = ("slug",)
    list_display = ("title","id","category")
    list_filter = ("is_bestseller",)

admin.site.register(Product,productAdmin)
admin.site.register(Brand)
admin.site.register(Address)
admin.site.register(Category)
# Register your models here.

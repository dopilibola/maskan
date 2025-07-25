from django.contrib import admin
from .models import Cemeterys, Grave, Person, Product, Category, ProductImage, Location

admin.site.register(Cemeterys)
admin.site.register(Grave)
admin.site.register(Person)
admin.site.register(Category)



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # 1ta bo‘sh rasm maydoni ko‘rsatadi
    min_num = 1
    max_num = 10  # Maksimal 10 ta rasm

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
admin.site.register(Location)


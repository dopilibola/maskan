from django.contrib import admin
from .models import Product, Category, ProductImage, Location, Qabristonmap, Qabristonmap_image



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
admin.site.register(Qabristonmap_image)

class QabristonmapAdmin(admin.ModelAdmin):
    list_display = (
        'ism_familiyasi_marhum',
        'years_old',
        'years',
        'years_new',
        'qator',
        'qabr_soni',
        'status',
        'product',
    )
    list_filter = ('status', 'product')
    search_fields = ('ism_familiyasi_marhum', 'qator', 'qabr_soni')

admin.site.register(Qabristonmap, QabristonmapAdmin)


    

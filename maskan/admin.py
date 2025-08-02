from django.contrib import admin
from .models import Product, Category, ProductImage, Location, Qabristonmap, Qabristonmap_image, UserAccess
from django.utils.html import format_html


admin.site.register(Category)



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1  # 1ta bo‘sh rasm maydoni ko‘rsatadi
    min_num = 1
    max_num = 10  # Maksimal 10 ta rasm



admin.site.register(Location)



class QabristonmapAdmin(admin.ModelAdmin):
    list_display = (
        'ism_familiyasi_marhum', 'years_old', 'years', 'years_new',
        'qator', 'qabr_soni', 'status', 'product'
    )
    list_filter = ('status', 'product')
    search_fields = ('ism_familiyasi_marhum', 'qator', 'qabr_soni')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            access = UserAccess.objects.get(user=request.user)
            return qs.filter(product__category__in=access.categories.all())
        except UserAccess.DoesNotExist:
            return qs.none()



class Qabristonmap_imageAdmin(admin.ModelAdmin):
    list_display = ('image_preview', 'product_name', 'cemetery_name', 'uploaded_at')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"
    image_preview.short_description = "Rasm"

    def product_name(self, obj):
        return obj.product.ism_familiyasi_marhum
    product_name.short_description = "Marhum Ismi"

    def cemetery_name(self, obj):
        return obj.product.product.name if obj.product.product else "Nomaʼlum qabriston"
    cemetery_name.short_description = "Qabriston nomi"

admin.site.register(Qabristonmap_image, Qabristonmap_imageAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'location_link', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        try:
            access = UserAccess.objects.get(user=request.user)
            return qs.filter(category__in=access.categories.all())
        except UserAccess.DoesNotExist:
            return qs.none()

    def location_link(self, obj):
        if obj.location:
            return format_html(
                '<a href="https://www.google.com/maps/search/?api=1&query={},{}" target="_blank">{}</a>',
                obj.location.latitude, obj.location.longitude, obj.location.name
            )
        return "-"
    location_link.short_description = "Lokatsiya (Google Maps)"



# admin.site.register(Product, ProductAdmin)




@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('product', 'image_preview', 'uploaded_at')
    readonly_fields = ('image_preview',)


@admin.register(UserAccess)
class UserAccessAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('categories',)
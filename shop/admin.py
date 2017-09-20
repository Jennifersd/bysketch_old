from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created', 'updated']
    #list_filter = ['available', 'created', 'updated']
    #list_editable = ['price', 'stock', 'available']
    #prepopulated_fields = {'slug': ('name',)}
    
    fieldsets = (
        ('Principal options', {
            'fields': ('name', 'slug', 'price', 'stock', 'available', 'category', 'image', 'description'),
        }),
        ('Advanced options', {
            'fields': ('free', 'document', 'support'),
        }),
    )
    list_editable = ['price', 'stock', 'available']
    list_filter = ['available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Product, ProductAdmin)

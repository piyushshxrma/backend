from django.contrib import admin
from django import forms
from .models import *
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',"name")
    search_fields = ["name"]
    ordering = ["name"]    
admin.site.register(Category,CategoryAdmin)
    

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id',"name","price","description","category")
    search_fields = ("name","category")
    
admin.site.register(Product,ProductAdmin)
    

class TableAdmin(admin.ModelAdmin):
    list_display = ('id',"number","is_available")
    search_fields = ("number","is_available")
admin.site.register(Table,TableAdmin)
    
    
class OrderItemtInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    autocomplete_fields = ('product',)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',"user","table","status","created_at","payment_method","total")
    search_fields = ("user","table","status","created_at","payment_method","total")
    list_editable = ("status","payment_method")
    
    inlines = [OrderItemtInline]
admin.site.register(Order,OrderAdmin)
    


# class OrderItemAdmin(admin.ModelAdmin):
#     list_display = ('user', 'product', 'quantity', 'price', 'price')
#     list_filter = ('user', 'product')
#     search_fields = ('order', 'product')


# admin.site.register(OrderItem, OrderItemAdmin)
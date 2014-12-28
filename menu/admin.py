#coding:utf8
from django.contrib import admin
from menu.models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	list_display = ("name","order",)
	search_fields = ("name",)

admin.site.register(Category, CategoryAdmin)


class MenuItemAdmin(admin.ModelAdmin):
	readonly_fields=("image_tag",)
	list_display = ('name', 'category','price','sold','recommend','creation_date_format',)
	fields = ('name', 'category','image','image_tag','price','sold','recommend',)
	list_filter = ('category','recommend',)
	search_fields = ("name",)

	def creation_date_format(self,obj):
		return obj.creation_date.strftime("%Y-%m-%d %H:%M:%S")
	creation_date_format.admin_order_field = 'creation_date'
	creation_date_format.short_description = u'菜品发布时间'

admin.site.register(MenuItem,MenuItemAdmin)
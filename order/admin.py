#coding:utf8
from django.contrib import admin
from order.models import Order
# Register your models here.


class OrderAdmin(admin.ModelAdmin):
	list_display = ('serial','items','seat','total','status','creation_date_format',)	
	date_hierarchy = 'creation_date'	
	def creation_date_format(self,obj):
		return obj.creation_date.strftime("%Y-%m-%d %H:%M:%S")
	creation_date_format.admin_order_field = 'creation_date'
	creation_date_format.short_description = u'订单生成日期'

	def last_modified_format(self,obj):
		return obj.creation_date.strftime("%Y-%m-%d %H:%M:%S")
	last_modified_format.admin_order_field = 'last_modified'
	last_modified_format.short_description = u'上一次修改日期'

	def items(self,obj):
		html = u"<table class='table' style='border:none;background:transparent;border-spacing:0;'>"
		tr=""
		for i in obj.cart.items.all():
			tr+=u"<tr style='border-spacing:0;'>"
			tr+=u"<td style='background:transparent;box-shadow:none;border:none;'>"+ i.menuitem.name+"</td>"
			tr+=u"<td style='background:transparent;box-shadow:none;border:none;'>"+  str(i.quantity) +"</td>"
			tr+=u"<td style='background:transparent;box-shadow:none;border:none;'>"+  str(i.get_price())  +"</td>"
			tr+=u"</tr>"
		html+=tr
		html+=u"</table>"
		return html
	items.short_description = u"产品列表"
	items.allow_tags = True

	def total(self,obj):
		return obj.cart.total()
	total.short_description = u"总计（元）"

admin.site.register(Order,OrderAdmin)
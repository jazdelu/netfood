from django.contrib import admin
from banner.models import Banner
# Register your models here.


class BannerAdmin(admin.ModelAdmin):
	readonly_fields=('image_tag',)
	list_display = ('image_tag','location',)
	fields = ('image','image_tag','location')

admin.site.register(Banner,BannerAdmin)
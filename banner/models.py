#coding:utf8
from django.db import models
from imagekit.processors import ResizeToFit, ResizeToFill
from imagekit.models import ImageSpecField
LOCATION_CHOICES = (
	('check',u'购物车页面'),
)

# Create your models here.
class Banner(models.Model):
	image = models.ImageField(upload_to ="banner/", verbose_name = u'上传图片',help_text = u'建议尺寸1200X180!')
	thumb_small = ImageSpecField(source='image',processors=[ResizeToFit(100)],format='JPEG',options={'quality': 80})
	thumb_big = ImageSpecField(source='image',processors=[ResizeToFill(1200,180)],format='JPEG',options={'quality': 80})
	location = models.CharField(max_length = 128, verbose_name = u'位置',default = 'check',choices = LOCATION_CHOICES)

	class Meta:
		verbose_name = u'广告'
		verbose_name_plural = u'广告'

	def __unicode__(self):
		return self.image.url

	def image_tag(self):
		return u'<img src = "%s"/>' % self.thumb_small.url 
	image_tag.short_description = u'预览图'
	image_tag.allow_tags = True
#coding:utf8
from django.db import models
from imagekit.processors import ResizeToFit, ResizeToFill
from imagekit.models import ImageSpecField
from django.core.files.images import get_image_dimensions
# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length = 128, verbose_name = u"分类名称")
	order = models.IntegerField(verbose_name = u"分类顺序")

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u"菜品分类"
		verbose_name_plural = u"菜品分类"
		ordering = ['order']

	def tab_link(self):
		s = "#tab"
		s+=str(self.id)
		print s
		return s

	def tab_id(self):
		s = "tab"
		s+=str(self.id)
		return s

class MenuItem(models.Model):
	name = models.CharField(max_length = 128, verbose_name = u"菜品名称")
	image = models.ImageField(upload_to = 'item/',verbose_name = u"菜品图片")
	thumb_small = ImageSpecField(source='image',processors=[ResizeToFit(100)],format='JPEG',options={'quality': 80})
	thumb_big_h = ImageSpecField(source='image',processors=[ResizeToFill(400,300)],format='JPEG',options={'quality': 80})
	thumb_big_v = ImageSpecField(source='image',processors=[ResizeToFill(200,300)],format='JPEG',options={'quality': 80})
	category = models.ForeignKey(Category, verbose_name = u"菜品分类",related_name = "items")
	price = models.FloatField(verbose_name = u"菜品价格")
	sold = models.IntegerField(verbose_name = u"售出份数",default = 0)
	recommend = models.BooleanField(verbose_name = u"是否设为推荐菜品？")
	creation_date = models.DateTimeField(auto_now_add = True)
	last_modified = models. DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.name

	def image_tag(self):
		return u'<img src = "%s"/>' % self.thumb_small.url 
	image_tag.short_description = u'预览图'
	image_tag.allow_tags = True

	def get_thumb(self):
		url = ''
		image =  self.image
		if image:
			w,h = get_image_dimensions(image)
			if w<h:
				url = self.thumb_big_v.url
			else:
				url = self.thumb_big_h.url
		return url



	class Meta:
		verbose_name = u"MY菜品"
		verbose_name_plural = u"MY菜品"
		ordering = ['-creation_date']

#coding:utf8
from django.db import models
from cart.models import Cart
# Create your models here.

STATUS_CHOICES = (
	("new",u"新订单"),
	("paid",u"已确认"),
	("discard",u"已作废"),
)

seat_default_errors = {
    'required': u'请输入一个有效的座位号!',
    'null': u'请输入一个有效的座位号!',
    'blank': u'请输入一个有效的座位号!',
}

class Order(models.Model):
	serial = models.CharField(max_length = 128,verbose_name = u"订单编号",blank = True, null = True)
	cart = models.ForeignKey(Cart)
	seat = models.IntegerField(verbose_name = u'座位号',error_messages = seat_default_errors)
	markup = models.CharField(max_length = 128,verbose_name = u'备注', blank = True,null  = True)
	status = models.CharField(max_length = 128,verbose_name = u'订单状态',choices = STATUS_CHOICES, default = "new",blank = True, null = True)
	creation_date = models.DateTimeField(auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)

	def __unicode__(self):
		return self.serial

	class Meta:
		verbose_name = u"订单"
		verbose_name_plural = u"订单"
		ordering = ['-creation_date']
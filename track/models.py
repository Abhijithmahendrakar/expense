from django.db import models
from django.utils import timezone
import datetime
# Create your models here.
class NewItem(models.Model):
	#newitem name
	name = models.CharField(max_length = 200, null = True)
	#item price
	price = models.IntegerField(null = True)
	#item image field
	image = models.FileField(blank = True, null = True)
	#Created_time
	Created_at = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		return self.name
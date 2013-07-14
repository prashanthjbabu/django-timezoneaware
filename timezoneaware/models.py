from django.db import models
import datetime
# Create your models here.

class stats(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    def __unicode__(self):
        return "%s %s" % (self.id,self.time)
    
from django.db import models
import uuid

# Create your models here.
class category(models.Model):
    id = models.UUIDField(default= uuid.uuid4,primary_key=True,null=False,editable=False)
    task_name = models.CharField(max_length=200,null=False, blank=False)
    description  = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)

class task(models.Model):
    id = models.UUIDField(default= uuid.uuid4,primary_key=True,null=False,editable=False)
    task_name = models.CharField(max_length=200,null=False, blank=False)
    description  = models.TextField(null=True,blank=True)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(category, on_delete=models.CASCADE,null=False)
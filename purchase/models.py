# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class PurchaseModel(models.Model):
    purchaser_name = models.CharField(max_length=20)
    quantity = models.IntegerField()


class PurchaseStatusModel(models.Model):
    purchase = models.ForeignKey(PurchaseModel)
    status = models.CharField(max_length=25,
                              choices=(("open", "Open"),
                              ("verified", "Verified"),
                              ("dispatched", "Dispatched"),
                              ("delivered", "Delivered"),
                              ))
    created_at = models.DateTimeField(auto_now_add=False)

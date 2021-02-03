# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import PurchaseModel, PurchaseStatusModel
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from django.http import JsonResponse
from dateutil.relativedelta import *

def index(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

# function for uploading data to the model
# currently exempting from security checks for development purposes
@csrf_exempt
def upload(request):
    if request.method == 'POST':
        data = json.loads(request.body) 
        purchase = data['purchase']
        statusUpdates = data['status']

        purchase = PurchaseModel.objects.create(purchaser_name=purchase['purchaser_name'], quantity=purchase['quantity'])
        for status in statusUpdates:
            created_at = datetime.datetime.strptime(status['created_at'], '%m/%d/%Y %H:%M')
            created_at = timezone.make_aware(created_at, timezone.get_current_timezone())
            purchaseStatus = PurchaseStatusModel.objects.create(purchase=purchase, status=status['status'], created_at=created_at)
        return HttpResponse(status=200)
    
    else:
        return HttpResponse(status=400)

# view to plot the cummulative quantity for each month
# currently exempting from security checks for development purposes
@csrf_exempt
def retrieveFrequency(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        startDate = data['start_date']
        startDate = timezone.make_aware(datetime.datetime.strptime(startDate, '%Y-%m-%d'), timezone.get_current_timezone())
        endDate = startDate + relativedelta(years=+1)

        # query to fetch data from the database as per the required filters
        itemList = PurchaseStatusModel.objects.filter(status__in=['Dispatched', 'Delivered']).filter(created_at__range=(startDate,endDate)).order_by('-status').select_related()
        
        # to check if dispatched of the same PurchaseModel id is used or not to decide for delivered
        dispatched = {}
        for item in itemList:
            if item.purchase.id not in dispatched:
                dispatched[item.purchase.id] = False

        # accumulation of data for each month in a single pass
        month = [0]*13
        for item in itemList:
            if not dispatched[item.purchase.id]:
                month[item.created_at.month] += item.purchase.quantity

        # creating a dictionary for data to send on payload
        month_data = {}
        for i in range(1, len(month)):
            month_data[i] = month[i]

        # payload to send to the frontend
        payload = {
            'month_d' : month_data,
            'start_date' : startDate.date(),
            'end_date' : endDate.date()
        }

        return JsonResponse(payload)
    
    else:
        return render(request, 'purchase/bar-simple.html')

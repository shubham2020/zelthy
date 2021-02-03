#!/usr/bin/env python3
import dateManipulationScript as dms
import random

class PurchaseStatusModelDataGeneration:

    def __init__(self):

        self.statuses = ["Open", "Verified", "Dispatched", "Delivered"]
        self.startDate = "1/1/2019 17:00"
        self.endDate = "3/31/2020 22:00"

    def randomStatuses(self):
        # create random number of statuses in chronological order for second part of json data to be
        # sent
        statuses = random.randint(1,4)
        statusList = []
        date = dms.random_date(self.startDate, self.endDate, random.random())
        for i in range(statuses):
            statusList.append({
                'status': self.statuses[i],
                'created_at': date
            })
            # to keep the order of status updates sorted in time
            if date != self.endDate:
                date = dms.random_date(date, self.endDate, random.random())
            else:
                break

        # print(statusList)
        return statusList

if __name__=='__main__':
    obj = PurchaseStatusModelDataGeneration()
    obj.randomStatuses()
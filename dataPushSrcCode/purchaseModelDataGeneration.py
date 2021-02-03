#!/usr/bin/env python3
import random
import sys
import json

# system recursion depth depth override with higher limit 
sys.setrecursionlimit(5000)

class PurchaseModelDataGeneration:

    def __init__(self):
        self.memo = {}
        self.numbers = []
        self.name = ["John", "Katy", "Tom", "Daniel", "Rambo", "Django", "Ross", "Kate", "Dustin", "Michael"]
        for i in range(1,11):
            self.memo[i] = 333
            self.numbers.append(i)

        random.shuffle(self.numbers)

    # function to calculate the data as per the given specifications
    def averageOfAverage(self, count, add, memoize={}):    
        if count < 0 or add < 0:
            return False

        if (count, add) in memoize:
            return memoize[(count, add)]

        if count == 0 and add == 0:
            return self.memo

        for i in self.numbers:
            possible = self.averageOfAverage(count-1, add-i)
            if possible:
                possible[i] += 1
                memoize[(count,add)] = possible
                return possible
            memoize[(count,add)] = possible

    def saveData(self, data):
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

    def loadData(self):
        with open('data.json') as json_file:
            data = json.load(json_file)
            return data

    # to jsonify the data
    def purchaseJSON(self):
        jsonList = []
        # to calculate data on the fly
        # data = self.averageOfAverage(1670, 16685)
        # to use the cached data from previous runs
        data = self.loadData()
        for i in data:
            for j in range(data[i]):
                jsonList.append({"purchaser_name":self.name[int(i)-1], "quantity": int(i)})

        random.shuffle(jsonList)
        return jsonList
        
if __name__=='__main__':
    
    obj = PurchaseModelDataGeneration()
    count = 1670
    add = 16685
    # value = obj.averageOfAverage(count, add)
    # obj.saveData(value)
    # print(value)

    # value = obj.loadData()
    print(obj.purchaseJSON())
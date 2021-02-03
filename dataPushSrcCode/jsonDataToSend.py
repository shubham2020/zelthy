#!/usr/bin/env python3

import purchaseModelDataGeneration as pmdg
import purchaseStatusModelDataGeneration as psmdg


class DataPreparation:

    def __init__(self):
        pass

    def getPMData(self):
        purchaseModel = pmdg.PurchaseModelDataGeneration()
        return purchaseModel.purchaseJSON()

    def getPSMData(self):
        purchaseStatusModel = psmdg.PurchaseStatusModelDataGeneration()
        return purchaseStatusModel.randomStatuses()

    def finalPayload(self):
        purchaseModels = self.getPMData()

        listOfDicts = []
        for purchaseModel in purchaseModels:
            listOfDicts.append({
                "purchase": purchaseModel,
                "status":self.getPSMData()
            })

        return listOfDicts

if __name__=='__main__':
    dp = DataPreparation()
    print(dp.finalPayload()[:10])
    print(len(dp.finalPayload()))
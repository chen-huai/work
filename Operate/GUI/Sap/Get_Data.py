import pandas as pd
import numpy as np

class Get_Data():
    def __init__(self,fileDataUrl):
        self.fileDataUrl = fileDataUrl
        # self.getFileData()
        # self.getHeaderData()
        # self.getIndexNumForHead()
        # self.getFileDataList()

    def getFileData(self):
        self.fileData = pd.read_excel(self.fileDataUrl)
        height, width = self.fileData.shape
        return self.fileData
    def getHeaderData(self):
        self.headData = list(self.fileData.head())
        return self.headData
    def getIndexNumForHead(self):
        self.projectNo = self.headData.index('Project No.')
        self.cs = self.headData.index('CS')
        self.sales = self.headData.index('Sales')
        self.currency = self.headData.index('Currency')
        self.partnerCode = self.headData.index('GPC Glo. Par. Code')
        self.materialCode = self.headData.index('Material Code')
        self.phyMaterialCode = self.headData.index('PHY Material Code')
        self.chmMaterialCode = self.headData.index('CHM Material Code')
        self.sapNo = self.headData.index('SAP No.')
        self.amount = self.headData.index('Amount')
        self.amountWithVAT = self.headData.index('Amount with VAT')
        self.exchangeRate = self.headData.index('Exchange Rate')
        self.costList = list(self.fileData['Total Cost'])
        return self.projectNo ,self.cs ,self.sales ,self.currency ,self.partnerCode ,self.materialCode ,self.phyMaterialCode ,self.chmMaterialCode ,self.sapNo ,self.amount ,self.amountWithVAT ,self.exchangeRate,self.costList
    def deleteTheRows(self, deleteList = {}):
        for key in deleteList:
            self.fileData = self.fileData[self.fileData[key] != deleteList[key]]
        return self.fileData
    def fillNanColumn(self,fillNanColumnKey):
        for filledKey in fillNanColumnKey:
            for fillKey in fillNanColumnKey[filledKey]:
                self.fileData[filledKey].fillna(self.fileData[fillKey], inplace=True)
        # self.fileData["Material Code"].fillna(self.fileData["PHY Material Code"], inplace=True)
        # self.fileData["Material Code"].fillna(self.fileData["CHM Material Code"], inplace=True)
        return self.fileData
    def pivotTable(self):
    # def pivotTable(self,pivotTableKey):
        self.fileData = pd.pivot_table(self.fileData,index=['CS', 'Sales', 'Currency', 'GPC Glo. Par. Code', 'Material Code'] , values = ['Amount', 'Amount with VAT', 'Total Cost'])
        return self.fileData
    def getFileDataList(self,getFileDataListKey):
        self.fileDataList = {}
        for each in getFileDataListKey:
            self.fileDataList[each] = list(self.fileData[each])
        return self.fileDataList
    def getFileDataList1(self):
        self.fileData = self.fileData[self.fileData['Amount'] != 0]
        # self.fileData.dropna(axis=0,subset=["Amount"],inplace = True)
        self.projectNoList = list(self.fileData['Project No.'])
        self.csList = list(self.fileData['CS'])
        self.salesList = list(self.fileData['Sales'])
        self.currencyList = list(self.fileData['Currency'])
        self.partnerCodeList = list(self.fileData['GPC Glo. Par. Code'])
        self.materialCodeList = list(self.fileData['Material Code'])
        self.sapNoList = list(self.fileData['SAP No.'])
        self.amountList = list(self.fileData['Amount'])
        self.amountWithVATList = list(self.fileData['Amount with VAT'])
        self.exchangeRateList = list(self.fileData['Exchange Rate'])
        self.costList = list(self.fileData['Total Cost'])
        return self.projectNoList, self.csList, self.salesList, self.currencyList, self.partnerCodeList, self.materialCodeList,self.sapNoList, self.amountList, self.amountWithVATList, self.exchangeRateList,self.costList

# deleteList = {'Amount': 0}
# a = Get_Data("C:\\Users\\chen-fr\\Desktop\\ODM4.xlsx")
# a.getFileData()
# a.deleteTheRows(deleteList)
# fillNanColumnKey = {'Material Code':["PHY Material Code", "CHM Material Code"]}
# a.fillNanColumn(fillNanColumnKey)
# a.pivotTable()
# getFileDataListKey = ['Project No.', 'CS', 'Sales', 'Currency', 'GPC Glo. Par. Code', 'Material Code', 'SAP No.', 'Amount', 'Amount with VAT', 'Exchange Rate', 'Total Cost']
# a.getFileDataList(getFileDataListKey)
# print(a)



import csv
import math
from collections import defaultdict
firstline= True
data_list=[]
ddict = {}
llist = []
month_quantity=[]
with open('data.csv','r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data_list.append(row)
Quantity1_list=[]
Quantity2_list=[]
Quantity3_list=[]
for index,row in enumerate(data_list):
    if index==0:
        columns=row
        # print("Columns",columns)
    else:
        month = int(row[0].split('-')[1])
        quantity = int(row[3])

        months = range(1, 13)
        for month in range(1,13):
            if row[1] == "Hot Chocolate Fudge":
                ddict[month] = llist
                llist.append(quantity)
            else:
                pass

        else:
            ddict[month]=month


print(ddict[3])
print(ddict[1])
print(ddict[2])




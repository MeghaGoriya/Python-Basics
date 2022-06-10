import csv
import math
from collections import defaultdict
from typing import Dict, List

firstline= True
data_list=[]

llist = []
month_wise: Dict[int, List[int]]={}

with open('data.csv','r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data_list.append(row)
for index,row in enumerate(data_list):
    if index==0:
        columns=row
        # print("Columns",columns)
    else:
        month = int(row[0].split('-')[1])
        quantity = int(row[3])

        # months = range(1, 13)
        # if month in range(1,13):
        #     if month in month_wise:
        #         month_wise
        #         if row[1] == "Hot Chocolate Fudge":
        #             month_wise[month] = llist
        #             llist.append(quantity)
        #         else:
        #             pass
        #     else:
        #         if row[1] == "Hot Chocolate Fudge":
        #
        #             month_wise[month] = llist
        #             llist.append(quantity)
        # else:
        #     pass

        if month in month_wise:
            month_wise_quantity=month_wise.get(month)
            if row[1] == "Hot Chocolate Fudge":
                month_wise[month] = llist
                llist.append(quantity)
            else:
                pass
            month_wise[month]=month_wise_quantity
        else:
            month_wise[month]={"Hot Chocolate Fudge":llist}
print(month_wise[1])
# print(month_wise[1])
print(month_wise[2])
print(month_wise[3])




import csv
import math
from collections import defaultdict
firstline= True
data_list=[]

llist = []
month_wise={}

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
        if month in range(1,13):
            if month in month_wise:
                if row[1] == "Hot Chocolate Fudge":
                    month_wise[month] = llist
                    llist.append(quantity)
                else:
                    pass
            else:
                pass
                # if row[1] == "Hot Chocolate Fudge":
                #     month_wise[month] = llist
                #     llist.append(quantity)
        else:
            pass

print(month_wise[1])
print(month_wise[2])
print(month_wise[3])




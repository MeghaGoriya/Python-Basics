import csv
import math
from collections import defaultdict
firstline= True
data_list=[]
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
        print("Columns",columns)
    else:
        month = int(row[0].split('-')[1])
        quantity=int(row[3])
        # print(type(data_list))
        if month == 1:
            # print("hey")
            if row[1]=="Hot Chocolate Fudge":
                 Quantity1_list.append(int(row[3]))
                 # print(Quantity_list)
        elif month==2:
            if row[1]=="Hot Chocolate Fudge":
                 Quantity2_list.append(int(row[3]))
        else:
            if row[1]=="Hot Chocolate Fudge":
                 Quantity3_list.append(int(row[3]))


print(Quantity1_list)
print(Quantity2_list)
print(Quantity3_list)
# print(month_quantity[2])
# # print(month_quantity[3])
month_wise_list={1:Quantity1_list,2:Quantity2_list,3:Quantity3_list}
for key, val in month_wise_list.items():
    summation=sum(val)
    length=len(val)
    average=int(summation/length)
    print(key ," ",max(val),min(val),average)






import csv
dic1 = {}
dic2 = {}
data=[]
month_wise_data={}
firstline = True
data_list=[]
with open('data.txt','r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data_list.append(row)

for index,row in enumerate(data_list):
    if index==0:
        columns=row
        print("Columns",columns)
    else:
        month=row[0].split("-")[1]
        price=int(row[4])
        sku=row[1]
        if month in month_wise_data:
            month_wise_sku=month_wise_data.get(month)
            if sku in month_wise_sku:
                month_wise_sku[sku]+=price
            else:
                month_wise_sku[sku]=price
            month_wise_data[month]=month_wise_sku
        else:
            month_wise_data[month]={sku:price}

print(month_wise_data)
# res = {}
# for key, val in month_wise_data.items():
#     max_val = 0
#     for ele in val.values():
#         if ele > max_val:
#             max_val = ele
#     res[key] = max_val
# print(res)
for key, val in month_wise_data.items():
        value = list(val.values())
        keys = list(val.keys())
        max_val = {key:{keys[value.index(max(value))]: max(value)}}
        data.append(max_val)

print(data)
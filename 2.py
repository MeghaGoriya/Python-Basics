import csv
dic1 = {}
dic2 = {}
firstline = True
data_list=[]
with open('data.txt',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data_list.append(row)
month_wise_data={}
for index,row in enumerate(data_list):
    if index==0:
        columns=row
        print("Columns",columns)
    else:
        month=row[0].rsplit("-",1)[0]
        quantity=int(row[3])
        sku=row[1]
        if month in month_wise_data:
            month_wise_sku=month_wise_data.get(month)
            if sku in month_wise_sku:
                month_wise_sku[sku]+=quantity
            else:
                month_wise_sku[sku]=quantity
            month_wise_data[month]=month_wise_sku
        else:
            month_wise_data[month]={sku:quantity}

print(month_wise_data)
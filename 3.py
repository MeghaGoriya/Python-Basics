import csv
month_data = {}
month_sku = {}
data=[]
firstline = True
with open('output.csv','r', newline='') as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        if firstline:
            firstline = False
            continue
        quantity = int(row[3])
        month = row[5]
        SKU = row[1]
        if month in month_data:
            month_sku=month_data.get(month)
            if SKU in month_sku:
                month_sku[SKU] += quantity
            else:
                month_sku[SKU] = quantity
            month_data[month] = month_sku
        else:
            # print("in sku")
            month_data[month] = {SKU:quantity}

    print(month_data)

    res = {}
    #
    # for key, val in month_data.items():
    #     max_val = 0
    #     for ele in val.values():
    #         # print(val.values())
    #         if ele > max_val:
    #             max_val = ele
    #     res[key] = max_val
    # print(res)
    for key, val in month_data.items():
        value = list(val.values())
        keys = list(val.keys())
        max_val = {key: {keys[value.index(max(value))]: max(value)}}
        data.append(max_val)
    print(data)





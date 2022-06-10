import csv
total_sum = {}
data_list=[]
firstline = True
with open('data.csv','r', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        data_list.append(row)

for index, row in enumerate(data_list):

    if index == 0:
        columns = row
        # print("Columns", columns)
    else:
        month = row[0].split("-")[1]
        total_price = int(row[4])
        if month not in total_sum:
            total_sum[month] = total_price
        else:
            total_sum[month] += total_price

print(total_sum)
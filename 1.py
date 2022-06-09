import csv
try:
    filename = open('data.csv', 'r')
except Exception as e:
    print("not able to open the file")
else:
     file = csv.DictReader(filename) # creating dictreader object
     Price = []                      # creating empty lists

     for col in file:
         # print("hey")
         Price.append(col['Total Price'])

     # print('Month:', Price)

Total_price=list(map(int, Price))
print(Total_price)
print(sum(Total_price))





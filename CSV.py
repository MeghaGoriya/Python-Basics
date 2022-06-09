# import csv module
import csv

# open the csv file with a context manager
with open('/home/megha/Downloads/ffffinal.csv', 'r') as csv_file:

  # using the csv reader function
  csv_reader = csv.reader(csv_file)

  # loop through the csv_reader iterable object
  for line in csv_reader:
    # print each line in the reader object
    print(line)




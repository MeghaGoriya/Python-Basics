from csv import writer
from csv import reader
def add_column_in_csv(input_file, output_file, transform_row):

    # Open the input_file in read mode and output_file in write mode
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        # Create a csv.reader object from the input file object
        csv_reader = reader(read_obj)
        # Create a csv.writer object from the output file object
        csv_writer = writer(write_obj)
        # Read each row of the input csv file as list
        for row in csv_reader:
            # Pass the list / row in the transform function to add column text for this row
            transform_row(row, csv_reader.line_num)
            # Write the updated row / list to the output file
            csv_writer.writerow(row)

# add_column_in_csv('data.csv', 'output_3.csv', lambda row, line_num: row.append(row[0].split('-')[1:2]))
# print(type(row))
header_of_new_col = 'Month'
add_column_in_csv('data.csv', 'output.csv',
                  lambda row, line_num: row.append(header_of_new_col) if line_num == 1 else row.append(*map(int,row[0].split('-')[1:2])))



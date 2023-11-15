import csv
header = ["id", "date", "category", "amount"]
with open('sales_data.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
data.insert(0, header)
with open('sales_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
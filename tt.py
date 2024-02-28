import json
import csv


# file = open("newText.txt", 'w')
# file.write("Hello world")
# print(file)
# file.close()

# with open("newText.txt") as file:
#     print(file.read())

with open('content.json', 'w') as file:
    data = {'nutan': [1, 2, 4], 'aditya': [6, 7, 8]}
    json.dump(data, file, indent=4, sort_keys=True)
    
with open('content.json', 'r') as f:
    data = json.load(f)
    print(type(data))
    
    str_data = json.dumps(data)
    print(str_data)
    print(type(str_data))
    
    print(json.loads(str_data))
    
# with open('demo.csv', 'r') as file:
    # csv_writer = csv.DictWriter(file, fieldnames=['Name', 'Age'], lineterminator="\n")
    # csv_writer.writeheader()
    # csv_writer.writerows({'Name': 'Nutan', 'Age': 22}, {'Name': 'Aditya', 'Age': 22})
    # csv_writer = csv.writer(file, lineterminator="\n")
    # csv_writer.writerow(['Name', 'Age'])
    # csv_writer.writerows([['Nutan', 22], ['Aditya', 22]])
    
    # reader = csv.DictReader(file)
    
    # for data in reader:
    #     print(data)
    
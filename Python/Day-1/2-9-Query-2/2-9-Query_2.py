import csv

try:
    with open('Query-2_inp.csv', encoding='utf-8-sig') as csv_file:
        input_file = csv.reader(csv_file, delimiter=',')
        flag = 0
        li = []
        for row in input_file:
            if flag == 0:
                key = row
                flag = 1
            else:
                value = row
                x = dict(zip(key, value))
                li.append(x)
        for i in li:
            print(i)
except():
    print('An Error Occurred')

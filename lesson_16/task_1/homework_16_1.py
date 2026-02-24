import csv

def load_csv(filepath:str) -> list:
    with open(filepath, newline='', encoding='utf-8') as file:
        return list(csv.reader(file))

data1, data2 = load_csv('r-m-c.csv'), load_csv('random.csv')
header = data1[0]
rows = data1[1:] + ([data2[0]] + data2[4:])[1:]

unique_rows = set(tuple(row) for row in rows)

with open('result_Fylyp.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(unique_rows)
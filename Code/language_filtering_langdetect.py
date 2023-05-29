from langdetect import detect
import csv

with open('C:\\PycharmProjects\\SMS\\cunique_new1.csv', encoding='utf8') as csv_file:

    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0

    for row in csv_reader:
        try:
            if line_count == 0:
                print(f'Column names are {"; ".join(row)}')
                line_count += 1
            else:
                # print(row[0])
                row_msg = row[0].split(',')
                # print(row_msg[0])
                lang = detect(row_msg[0])
                print(lang + "::" + row_msg[0])
                if lang == "en":
                    employee_file = open('cunique_new1_En.csv', mode='a')
                    csv_reader = csv.reader(csv_file, delimiter=';')
                    employee_writer = csv.writer(employee_file)
                    employee_writer.writerow(row)
                    employee_file.close()
                    line_count += 1
        except:
            pass
    print(f'Processed {line_count} lines.')
















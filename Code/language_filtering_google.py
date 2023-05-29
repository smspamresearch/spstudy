import asyncio
import async_google_trans_new
import csv

async def coro():
    g = async_google_trans_new.AsyncTranslator()
    #print(await g.translate("こんにちは、世界！","en"))
    with open('C:\\PycharmProjects\\SMS\\ds7_en_test.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        for row in csv_reader:
            row_msg = row[0].split(',')
            print(row_msg[1])
            lang = await g.detect(row_msg[1])
            print(lang[1] + "::" + row_msg[1])
            if lang[1]=="english":
                employee_file = open('ds7_en_google1.csv', mode='a')
                csv_reader = csv.reader(csv_file, delimiter=';')
                employee_writer = csv.writer(employee_file)
                employee_writer.writerow(row)
                employee_file.close()
                line_count += 1
        print(f'Processed {line_count} lines.')
loop = asyncio.get_event_loop()
loop.run_until_complete(coro())




import json
import csv
# import csv
# import unicodecsv as csv

with open('KPOP2018_pretty.json', 'r') as data_file:
    data = json.load(data_file)

csvFile = open('KPOP2018.csv', 'w', encoding="utf-8", newline='')
wr = csv.writer(csvFile)
# with open('test123123123.csv', 'wb') as
    # writer = csv.writer(csv_file, encoding="utf-8", newline=" ")

wr.writerow(["fullname","html","id","like","replies","retweets","text","timestamp","url","user"])

for row in data:
    # wr.writerow([row["timestamp"],row["text"]])
    wr.writerow([row["fullname"],row["html"],row["id"],row["likes"],row["replies"],row["retweets"],row["text"],row["timestamp"],row["url"],row["user"],])

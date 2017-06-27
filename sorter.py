import sys, csv
from collections import OrderedDict
ordered_fieldnames = OrderedDict([('Title', None),('Price', None),('City', None),('URL',None)])
a = ['nightstand', 'night stand', 'computer desk', 'computerdesk'] 
with open('results.csv', 'rb') as csvfile:
    with open('clean.csv', 'wb') as fou:
        listwriter = csv.DictWriter(fou, delimiter=',', fieldnames=ordered_fieldnames)
        listwriter.writeheader()
        listreader = csv.DictReader(csvfile, delimiter=',')
        for row in listreader:
            for k, v in row.items():
                if any(x in v for x in a):
                    listwriter.writerow({'Title':row['Title'],'Price':row['Price'], 'City':row['City'], 'URL':row['URL']})

import csv

indiascore = input("score of india")
englandscore = input("score of england")

with open('user_data.csv', mode='a') as csv_file:
    fieldnames = ['indiascore','englandscore']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)



    writer.writerow({'indiascore': indiascore, 'englandscore': englandscore,})

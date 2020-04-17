import csv

with open("CSV/firstData.csv", "w", newline='') as csvFile:
    obj = csv.DictWriter(csvFile, fieldnames=["FirstCol", "SecondCol"])
    obj.writeheader()
    obj.writerow({"FirstCol": "Day 1", "SecondCol": "Python Completed"})
    obj.writerow({"FirstCol": "Day 2", "SecondCol": "Python In progress"})
    obj.writerow({"FirstCol": "Day 3", "SecondCol": "Python Planned"})
    csvFile.close()

with open("CSV/firstData.csv", newline='') as csvFile:
    objReader = csv.DictReader(csvFile, fieldnames=None)
    for row in objReader:
        print(row['FirstCol'], row['SecondCol'])
    csvFile.close()

help(csv.DictReader)
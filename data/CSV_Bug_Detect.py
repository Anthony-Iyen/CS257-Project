import csv
import sys


filename = sys.argv[1]
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] != "Animalia":
            print(row[0])



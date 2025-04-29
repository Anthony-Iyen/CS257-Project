import csv
import sys


filename = sys.argv[1]
writer = csv.writer(sys.stdout)
with open(filename) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[1] != "Animalia":
            writer.writerow(row)



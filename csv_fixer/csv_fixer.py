from tempfile import NamedTemporaryFile
import shutil
import csv
import sys

args = sys.argv
filename = args[1]
new_filename = 'fixed_' + filename

tempfile = NamedTemporaryFile('w+t', newline='', delete=False)

with open(filename, 'r', newline='') as csvFile, tempfile:
    reader = csv.reader(csvFile, delimiter=',')
    writer = csv.writer(tempfile, delimiter=',')

    for row in reader:
        row[1] = row[1].title()
        row[5] = '="' + row[5] + '"'
        print(row[5])
        writer.writerow(row)

shutil.move(tempfile.name, new_filename)

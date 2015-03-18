#To be able to read csv formated files, we will first have to import the
#csv module.
import csv

csv_file = "RightTurnData.csv"

A_X, A_Y, G_X, G_Y, T = 0, 1, 3, 4, 6

CSV_DATA = [[0, 0, 0, 0, 0, 0, 0]]
dVelocity = [[0, 0]]
dPosition = []

with open(csv_file, 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if (row[0] != ""):
            CSV_DATA.append(row)

for index, row in enumerate(CSV_DATA[1:]):
    a_last = ((CSV_DATA[index - 1][A_X] ** 2) + (CSV_DATA[index - 1][A_Y] ** 2)) ** .5
    a_this = ((row[A_X] ** 2) + (row[A_Y] ** 2)) ** .5
    dVelocity[index] = [ (a_this * row[T]) - (a_last * CSV_DATA[index - 1][T]) , row[T] ]

for vel in dVelocity:
    print vel

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
    reader.next()
    for row in reader:
        if (row[0] != ""):
            CSV_DATA.append([float(x) for x in row])

for index, row in enumerate(CSV_DATA[1:]):
    this_time = row[T] * (10 ** -3)
    last_time = CSV_DATA[index - 1][T] * (10 ** -3)
    a_last = ((CSV_DATA[index - 1][A_X] ** 2) + (CSV_DATA[index - 1][A_Y] ** 2)) ** .5
    a_this = ((row[A_X] ** 2) + (row[A_Y] ** 2)) ** .5
    dVelocity.append([ (a_this * this_time) - (a_last * last_time) , this_time ])

for index, row in enumerate(dVelocity[1:]):
    dPosition.append((row[0] * row[1]) - (dVelocity[index - 1][0] * dVelocity[index - 1][1]))

print sum(dPosition)

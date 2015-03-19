#To be able to read csv formated files, we will first have to import the
#csv module.
import csv

def calc_distance(accelerations):
    di = 0.0
    vi = 0.0

    for index, row in enumerate(accelerations[1:]):
        di += (accelerations[index][0] - accelerations[index - 1][0]) * (accelerations[index][1] - accelerations[index - 1][1])

    return di

csv_file = "RightTurnData.csv"

A_X, A_Y, T = 0, 1, 6

CSV_DATA = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
x_accelerations = [[0.0, 0.0]]
y_accelerations = [[0.0, 0.0]]

with open(csv_file, 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        if (row[0] != ""):
            time = float(row[T]) * (10**-3) # mS to S
            x_accelerations.append([float(row[A_X]), time])
            y_accelerations.append([float(row[A_Y]), time])

x_dis = calc_distance(x_accelerations)
y_dis = calc_distance(y_accelerations)

print (x_dis + y_dis) / 2



#To be able to read csv formated files, we will first have to import the
#csv module.
import csv

def calc_distance(data):
    a, v, t = 0, 0, 1
    delta_v = [[0, 0]]
    delta_p = [0]

    #first integration
    for n, e in enumerate(data):
        if (n == 0):
            continue

        velocity = delta_v[n - 1][v] + data[n - 1][a] * ( data[n][t] - data[n - 1][t] )
        delta_v.append( [velocity, data[n][t]] )

    #second integration
    for n, e in enumerate(delta_v):
        if (n == 0):
            continue

        delta_t = delta_v[n][t] - delta_v[n - 1][t];
        position = delta_p[n - 1] + delta_v[n - 1][v] * delta_t + .5 * data[n - 1][a] * (delta_t ** 2)
        delta_p.append(position)

    return delta_p[-1]

csv_file = "RightTurnData.csv"

A_Y, T = 1, 6

y_accelerations = [[0.0, 0.0]]

with open(csv_file, 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        if (row[0] != ""):
            time = float(row[T]) * (10**-3) # mS to S
            y_accelerations.append( [float(row[A_Y]), time] )

y_dis = calc_distance(y_accelerations)

print 'X is: %e' % (abs(y_dis / 2))



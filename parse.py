#To be able to read csv formated files, we will first have to import the
#csv module.
import csv

A_Y, G_Z, T = 1, 5, 6
y_accelerations = [[0.0, 0.0]]

# Calculate the distance in a specific direction by double integrating the data over time
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

def right_turn():
    csv_file = "RightTurnData.csv"

    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            if (row[0] != ""):
                time = float(row[T]) * (10**-3) # mS to S
                y_accelerations.append( [float(row[A_Y]), time] )

    y_dist = calc_distance(y_accelerations)
    print 'X is: %e' % (abs(y_dist / 2))

def multiple_turn():
    csv_file = "MultipleTurnData.csv"
    turn_threshold = 0.08
    z_gyroscope = [[0, 0]]

    with open(csv_file, 'rb') as f:
        reader = csv.reader(f)
        reader.next()
        for row in reader:
            if (row[0] != ""):
                time = float(row[T]) * (10**-3) # mS to S
                y_accelerations.append( [float(row[A_Y]), time] )
                z_gyroscope.append( [float(row[G_Z]), time] )

    y_dist = calc_distance(y_accelerations)
    print 'Y is: %e' % (abs(y_dist / 5))

    last = 0.0
    this_turn = [[0.0, 0.0]]
    turn_data = []
    for index, [gyro, time] in enumerate(z_gyroscope):
        if (abs(gyro) > turn_threshold):
            this_turn.append( [gyro, time] )
        elif (this_turn[-1][1] == z_gyroscope[index - 1][1]):
            if (len(this_turn) > 1):
                turn_data.append(this_turn)

            this_turn = [[0.0, 0.0]]

    radians = [0.0, 0.0, 0.0, 0.0]
    for i, turn in enumerate(turn_data):
        for j, [gyro, time] in enumerate(turn):
            if (j == 0):
                continue

            #print gyro * (time-turn[j-1][1])
            radians[i] += (gyro * (time - turn[j-1][1]))

    print radians

right_turn()
multiple_turn()

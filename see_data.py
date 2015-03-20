#To be able to read csv formated files, we will first have to import the
#csv module.
import csv
import matplotlib.pyplot as p

csv_file1 = "RightTurnData.csv"
csv_file2 = "MultipleTurnData.csv"

A_X, A_Y, A_Z, G_X, G_Y, G_Z, T = 0, 1, 2, 3, 4, 5, 6

CSV_DATA = [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
x_a = []
y_a = []
z_a = []
x_g = []
y_g = []
z_g = []

with open(csv_file2, 'rb') as f:
    reader = csv.reader(f)
    reader.next()
    for row in reader:
        if (row[0] != ""):
            time = float(row[T]) * (10**-3) # mS to S
            x_a.append(row[A_X])
	    y_a.append(row[A_Y])
            z_a.append(row[A_Z])
            x_g.append(row[G_X])
            y_g.append(row[G_Y])
            z_g.append(row[G_Z])

p.figure(figsize=[13,8])
p.subplot(321)
p.plot(x_a)
p.ylabel('x accel (m / s^2)')

p.subplot(323)
p.plot(y_a)
p.ylabel('y accel (m / s^2)')

p.subplot(325)
p.plot(z_a)
p.ylabel('z accel (m / s^2)')

p.subplot(322)
p.plot(x_g)
p.ylabel('x ang accel (rad / s^2)')

p.subplot(324)
p.plot(y_g)
p.ylabel('y ang accel (rad / s^2)')

p.subplot(326)
p.plot(z_g)
p.ylabel('z ang accel (rad / s^2)')
p.savefig('MultipleTurnProfiles.png',bbox_inches='tight')

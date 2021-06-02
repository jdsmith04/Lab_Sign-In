import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt

# TODO: read from excel
# TODO: convert from excel to csv

# read in csv file
csv = pd.read_csv('Sign-in Sheet.csv')
print(csv)

# formatting TimeIn and TimeOut
csv['TimeIn'] = pd.to_datetime(csv.TimeIn)
csv['TimeOut'] = pd.to_datetime(csv.TimeOut)

# converting csv.TimeIn and csv.TimeOut to datetime lists
time_in = []
time_out = []
for a in range(len(csv)):
    time_in.append(csv.TimeIn[a])
    time_out.append(csv.TimeOut[a])
    time_in[a] = datetime.strptime(str(time_in[a]), '%Y-%m-%d %H:%M:%S')
    time_out[a] = datetime.strptime(str(time_out[a]), '%Y-%m-%d %H:%M:%S')

visitors_per_hour = {'9:00': 0, '10:00': 0, '11:00': 0, '12:00': 0, '13:00': 0, '14:00': 0, '15:00': 0, '16:00': 0,
                     '17:00': 0, '18:00': 0, '19:00': 0, '20:00': 0, '21:00': 0}

# figuring out number of students in lab at given hour
for a in range(len(time_in)):
    start = time_in[a].hour
    end = time_out[a].hour
    for b in range(start, end + 1):
        if b == 9:
            visitors_per_hour['9:00'] += 1
        if b == 10:
            visitors_per_hour['10:00'] += 1
        if b == 11:
            visitors_per_hour['11:00'] += 1
        if b == 12:
            visitors_per_hour['12:00'] += 1
        if b == 13:
            visitors_per_hour['13:00'] += 1
        if b == 14:
            visitors_per_hour['14:00'] += 1
        if b == 15:
            visitors_per_hour['15:00'] += 1
        if b == 16:
            visitors_per_hour['16:00'] += 1
        if b == 17:
            visitors_per_hour['17:00'] += 1
        if b == 18:
            visitors_per_hour['18:00'] += 1
        if b == 19:
            visitors_per_hour['19:00'] += 1
        if b == 20:
            visitors_per_hour['20:00'] += 1
        if b == 21:
            visitors_per_hour['21:00'] += 1
print(visitors_per_hour)

# TODO: add in class labs per weekday (25 students)
# TODO: timestamp x axis
# x axis
lab_hours = [k for k in visitors_per_hour]
# y axis
visitor_data = [v for v in visitors_per_hour.values()]
# y axis ticks
number_of_students = [i for i in range(24 + 1)]

# TODO: add in chart title
plt.style.use('seaborn')
plt.plot_date(lab_hours, visitor_data, linestyle='solid')
plt.gcf().autofmt_xdate()
plt.yticks(number_of_students)
plt.ylabel('number of students in lab')
plt.xlabel('lab hours')

plt.show()
# TODO: send charts to powerpoint
# TODO: email powerpoints

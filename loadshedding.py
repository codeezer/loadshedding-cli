import getTables
import re
import colors as c

tables = getTables.getTables()
times = []
days = []
for row in tables[1:8]:
    for each_day in row:
        times.append(re.split('\n| ',each_day))
count = 0
for time in times:
    if count == 8:
        count = 0
    if count == 0:
        print(c.END+time[0]+' '+time[1])
    else:
        print(c.ORANGE+tables[0][count],end = '\t'+c.END)
        for row in time:
            print(c.CYAN+row,end = ' '+c.CYAN)
        print('\n')
    count = count + 1

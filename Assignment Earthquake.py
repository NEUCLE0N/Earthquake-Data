#190051232 Assignemnt Earthquakes


#Intitalizing Lists
earthquakes = [[1845, 8, 6], [1846, 10, 18], [1850, 5, 7], [1851, 2, 9], [1852, 5, 1], [1858, 3, 16], [1861, 2, 16],
               [1862, 6, 18], [1863, 3, 29], [1863, 6, 8], [1863, 8, 11], [1866, 1, 23], [1866, 5, 23], [1869, 1, 10],
               [1869, 1, 10]]
earthquakes = sorted(earthquakes)
aftershocks = []
mainQuakes = []
#Initializing variables
yearCur = 0
monthCur = 0
dayCur = 0
yearPrev = 0
monthPrev = 0
dayPrev = 0

for x in earthquakes:
    yearCur = x[0]
    monthCur = x[1]
    dayCur = x[2]

    if yearCur == yearPrev:                                                                  #check if they are in same year
        if (monthCur == monthPrev) and (dayCur - dayPrev < 6):                               # checks if month same and days apart less than 6
            aftershocks.append(yearCur)
        else:
            mainQuakes.append(yearCur)

        if (monthCur == monthPrev + 1) and ((dayCur + 30) - dayPrev < 6):                   #checks if month is different but still less than 6 days apart
            aftershocks.append(yearCur)
        else:
            mainQuakes.append(yearCur)

    elif yearCur == yearPrev + 1:
        if ((monthPrev + 1) == 13) and (monthCur == 1) and ((dayCur + 30) - dayPrev < 6):   #checks if year different but still less than 6 days apart
            aftershocks.append(yearCur)
            break

    else:
        mainQuakes.append(yearCur)

    yearPrev = yearCur
    monthPrev = monthCur
    dayPrev = dayCur

print("The year(s) with main quakes:\n")
for y in mainQuakes:
    print(y)

print("\nThe year(s) with aftershocks:\n")
for y in aftershocks:
    print(y)
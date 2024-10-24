from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Chapter-16-DownloadingData/weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#Extract high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[header_row.index('DATE')], '%Y-%m-%d')
    try:
        high = int(row[header_row.index('TMAX')])
        low = int(row[header_row.index('TMIN')])
        stationname=str(row[header_row.index('NAME')])
    except ValueError:
        print(f'Missing data for {current_date}')
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#print(highs)

#plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#alpha argument controls a color's transparency
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot.
title = f'Daily High and Low Temperatures, 2021\n {stationname}'
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

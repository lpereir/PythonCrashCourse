from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Chapter-16-DownloadingData/weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

#Extract high temperatures.
dates, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[4])
    low = int(row[5])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)

path2 = Path('Chapter-16-DownloadingData/weather_data/death_valley_2021_simple.csv')
lines2 = path2.read_text().splitlines()

reader2 = csv.reader(lines2)
header_row2 = next(reader2)

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

#Extract high temperatures.
dates2, highs2, lows2 = [], [], []
for row in reader2:
    current_date2 = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high2 = int(row[3])
        low2 = int(row[4])
    except ValueError:
        print(f'Missing data for {current_date2}')
    else:
        dates2.append(current_date2)
        highs2.append(high2)
        lows2.append(low2)

#print(highs)

#plot the high and low temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#alpha argument controls a color's transparency
ax.plot(dates2, highs2, color='yellow', alpha=0.5)
ax.plot(dates2, lows2, color='darkblue', alpha=0.5)
ax.fill_between(dates2, highs2, lows2, facecolor='darkblue', alpha=0.1)

ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

#Format plot.
ax.set_title('Daily High and Low Temperatures, 2021\nDeath Valley, CA and Sitka, Alasca', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.set(ylim=(0,150))
ax.tick_params(labelsize=16)

plt.show()

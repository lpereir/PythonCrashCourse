from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

path = Path('Chapter-16-DownloadingData/weather_data/death_valley_2021_full.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

#Extract daily rainfall amounts.
dates, rainfalls = [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    rainfall = float(row[5])
    dates.append(current_date)
    rainfalls.append(rainfall)

#print(highs)

#plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, rainfalls, color='red')

#Format plot.
ax.set_title('Daily Rainfall Amounts, 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel('Amounts', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()
from pathlib import Path
import csv

import matplotlib.pyplot as plt

path = Path('Chapter-16-DownloadingData/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

#for index, column_header in enumerate(header_row):
#    print(index, column_header)

#Extract high temperatures.
highs = []
for row in reader:
    high = int(row[4])
    highs.append(high)

#print(highs)

#plot the high temperatures.
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(highs, color='red')

#Format plot.
ax.set_title('Daily High Temperatures, July 2021', fontsize=24)
ax.set_xlabel('', fontsize=16)
ax.set_ylabel('Temperature (F)', fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

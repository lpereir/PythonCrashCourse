from pathlib import Path
import json

#read data as a string to converto to a python object
path = Path('Chapter-16-DownloadingData/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

#Examine all earthquakes in the dataset
all_eq_dicts = all_eq_data['features']

mags, lons, lats=[],[],[]
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(lons[:5])
print(lats[:5])

#create a more readable version of data file
#path = Path('Chapter-16-DownloadingData/eq_data/readable_eq_data.geojson')
#readable_contents = json.dumps(all_eq_data, indent=4)
#path.write_text(readable_contents)
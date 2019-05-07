import csv
from matplotlib import pyplot as plt
from datetime import datetime

file_name = './sitka_weather_2014.csv'

with open(file_name) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:

        dates.append(datetime.strptime(row[0], "%Y-%m-%d"))

        highs.append(int(row[1]))

        lows.append(int(row[3]))



# Faz a plotagem dos dados
fig = plt.figure(dpi=128, figsize=(10, 6))

plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

plt.title("Daily high and low temperatures - 2014", fontsize=24)
plt.xlabel('', fontsize=16)

fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
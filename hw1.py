# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061124.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
#target_data = data[:10]

target = []
stations = ['C0A880', 'C0F9A0','C0G640', 'C0R190', 'C0X260']
#stations = ['C0A880', 'C0F9A0','C0G640', 'C0R190', 'C0X260', 'A']
for station in stations:
   target_data = list(filter(lambda item: item['station_id'] == station, data))
   sum = 0.0
   num = 0
   for item in target_data:
      if (item['PRES'] != '-99.000') and (item['PRES'] != '-999.000'):
         sum += float(item['PRES'])
         num += 1
   if num > 0:
      mean = sum/num
      target.append([station, round(mean, 2)])
   else:
      target.append([station, 'None'])
#=======================================

# Part. 4
#=======================================
# Print result

#target.sort()
print(sorted(target))
#print(target)

#========================================








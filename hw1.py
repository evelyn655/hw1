# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108061101.csv'
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

#=======================================

# Part. 4
#=======================================
# Print result

#print(target_data)

#========================================

'''
tmp = 0
for item in data:
   if (item['PRES'] == '-99.000'):
      tmp += 1
      print(item['station_id'], item['PRES'])
print(tmp)
'''

target = []




target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))
sum = 0.0
num = 0
for item in target_data:
   if item['PRES'] != '-99.000' and item['PRES'] != '-999.000':
      sum += float(item['PRES'])
      num += 1
if num > 0:
   mean = sum/num
   target.append(['C0F9A0', round(mean, 2)])
else:
   target.append(['C0F9A0', 'None'])


target_data = list(filter(lambda item: item['station_id'] == 'C0G640', data))
sum = 0.0
num = 0
for item in target_data:
   if item['PRES'] != '-99.000' and item['PRES'] != '-999.000':
      sum += float(item['PRES'])
      num += 1
if num > 0:
   mean = sum/num
   target.append(['C0G640', round(mean, 2)])
else:
   target.append(['C0G640', 'None'])


target_data = list(filter(lambda item: item['station_id'] == 'C0R190', data))
sum = 0.0
num = 0
for item in target_data:
   if item['PRES'] != '-99.000' and item['PRES'] != '-999.000':
      sum += float(item['PRES'])
      num += 1
if num > 0:
   mean = sum/num
   target.append(['C0R190', round(mean, 2)])
else:
   target.append(['C0R190', 'None'])


target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
sum = 0.0
num = 0
for item in target_data:
   if item['PRES'] != '-99.000' and item['PRES'] != '-999.000':
      sum += float(item['PRES'])
      num += 1
if num > 0:
   mean = sum/num
   target.append(['C0X260', round(mean, 2)])
else:
   target.append(['C0X260', 'None'])





target_data = list(filter(lambda item: item['station_id'] == 'C0A880', data))
sum = 0.0
num = 0
for item in target_data:
   if (item['PRES'] != '-99.000') and (item['PRES'] != '-999.000'):
      sum += float(item['PRES'])
      num += 1
if num > 0:
   mean = sum/num
   target.append(['C0A880', round(mean, 2)])
else:
   target.append(['C0A880', 'None'])

#target.sort()
print(sorted(target))
print(target)
# use for loop, please
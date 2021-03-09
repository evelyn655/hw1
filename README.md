# HW1 Python Data Analysis
Find out the mean of the pressure values from the station C0A880, C0F9A0, C0G640, C0R190 and C0X260

## How to set up and run my program
1. Read the data by the sample code provided
2. Data analysis
```
target = []
stations = ['C0A880', 'C0F9A0','C0G640', 'C0R190', 'C0X260']                      // store target stations in a list

for station in stations:                                                          // run through every target station
   target_data = list(filter(lambda item: item['station_id'] == station, data))   // retrive all data points for specific station_id 
   sum = 0.0
   num = 0  
   for item in target_data:                                                       // run through each data 
      if (item['PRES'] != '-99.000') and (item['PRES'] != '-999.000'):            // filter out the unwanted data
         sum += float(item['PRES'])                                               // sum each data
         num += 1                                                                 // and count the number of data
   if num > 0:
      mean = sum/num                                                              // compute the average
      target.append([station, round(mean, 2)])                                    // add the computation result to the list 
   else:
      target.append([station, 'None'])                                            // if there is no data for specific station_id, output 'None'
```
3. Output the result
```
print(sorted(target))            // Output the results in the lexicographical order
```

## The results
```
// result for 108061124.csv
[['C0A880', 1014.18], ['C0F9A0', 967.12], ['C0G640', 1015.93], ['C0R190', 1010.8], ['C0X260', 1011.18]]
```

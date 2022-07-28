# surfs_up

## Overview of the statistical analysis:

For this project, the use of programming tools will be implemented in order to thoroughly analyze the climate data in Oahu, with an emphasis on June and December. These programming tools include SQLite, SQLAlchemy, and Flask, the data provided from these tools can be utilized in order to pursue a location that fits the needs of a ice cream and surf shop. gathering the data from both June and December will help give an idea on the year round sustainability that each shop will have in accordance to their locations temperature range over the years

## Results:
figure 1: June Temperature Statistics

![June_Temps](https://github.com/Calebmkelly/surfs_up/blob/main/Resources/June_Temps.png)

figure 2: December Temperature Statistics

![Dec_Temps](https://github.com/Calebmkelly/surfs_up/blob/main/Resources/Dec_Temps.png)

figure 1 June Temps:
- Count: 1700
- Mean: 74.944
- Standard deviation: 3.257
- Minimum: 64
- 25 Percentile: 73
- 50 percentile: 75
- 75 percentile: 77
- Maximum: 85

figure 2 Dec Temps:
- Count: 1517
- Mean: 71.042
- Standard deviation: 3.746
- Minimum: 56
- 25 Percentile: 69 
- 50 percentile: 71
- 75 percentile: 74
- Maximum: 83

Above are the results in image form and in text. The data seems to differ in every aspect, taking a closer look at three components, Minimum, Average, and Maximum can elucidate a more clear idea as too wether or not the temperatures extracted are in a good range that suits a surf/ice cream shop. In Fahrenheit, June has a minimum temperature of 64 degrees, an average temperature of around 75 degrees, and a maximum temperature of 85 degrees. For the month of December, there is a minimum temperature of 56 degrees, an average temperature of around 71 degrees, and a maximum temperature of 83 degrees.

## Summary:

Taking a look at the results, both June and December have promising temperatures. Although the minimum temperatures for both June and December, 64 and 56, are quite low for "Ice Cream" temperatures, this point of data should not be discouraging as the average temperature for both months is above 70 degrees Fahrenheit. in addition, the minimum temperature is three standard deviations away from the mean for both months, providing that minimum temperature is close to being an outlier. furthermore, both months have the 25 percentile around 70 degrees, this illustrates how most of the data is in a preferred range for both shops. 

while the temperatures look great, developing queries to find the the precipitation rate for each month can help bring a better understanding of the wheather conditions in Oahu, as many people may not like surfing or eating ice cream in the rain.

Below is a screen shot of two queries that can be run: the first query grabs the precipitation data from june, the second query grabs precipitation data from December.

![Additional_Queries.png](https://github.com/Calebmkelly/surfs_up/blob/main/Resources/Additional_Queries.png)

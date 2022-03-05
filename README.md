# Surf's Up!
Climate analysis of Oahu to determine ice cream and surfing sales.

## Overview of Hawaii Temperature Analysis:

This analysis was performed using sqlite and sqlalchemy to query weather data for the months of June and December over serveral years in Oahu. This analysis will show if it is sustainable to sell ice cream and surf supplies all year round.

## Results:

For the months of June and December, we saw three key differences
- The lowest recorded temperature for the month of December is 56°, whereas the lowest recorded temperature for the month of June is 64°F
- However, for highest recorded temperature, the two months are not that different from each other (85°F for June vs. 83°F for December)
- The temperatures in the four quartiles for June are very similar, there is not much temperature variation for the month of June. In contrast, there is a somewhat larger range for the December temperatures.

## Summary:

Based on the results, there is not much temperature variation between June and December. Based on temperature alone, which is about 70-75°F all year round, it would be sustainable to sell ice cream and surf supplies all year. However, temperature alone does not dictate wheather or not people will be inclined to surf or buy ice cream. For example, a query of precipitation data for the months of June and December would help show when the rainy months were. People are less inclined to buy ice cream or surf when it is raining. Wind speed would be another useful metric to take into consideration, since high wind days will see less people buying ice cream but potentially more people surfing.

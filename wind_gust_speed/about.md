# About the Anemometer

This is the anemometer sensor supplied with the Raspberry Pi Weather Station kit. It is used to measure wind gust speed.

![Anemometer](images/anemometer.png)

## How does it work?

You have already explored the inside of the anemometer in the wind speed lesson. 

Gusts of wind are sudden brief increases in the speed of the wind. 

According to U.S. weather observing practice, gusts are reported when the peak wind speed reaches at least 16 knots and the variation in wind speed between the peaks and lulls is at least 9 knots. The duration of a gust is usually less than 20 seconds. 

16 knots is approximately 29.6km/h, and 9 knots is 16.7km/h

(Note: Recommend 5 and 2 for testing)

We can use this information to calculate when gusts appear using three rules:
A gust occurs within a given time period when:
- the highest wind speed measured during a period is above 29.6km/h AND
- the difference between the peak speed and lowest speed in that period is greater than 16.7km/h AND
- the time period is 20 seconds or less

We will measure the wind speed as before, but this time we will store a range of values, allowing us to calculate whether a gust has occurred within the last 20 second time period.

The following algorithm can be used to calculate the gust speed:

>   Pseudo code here

## How does the sensor connect?

To connect the anemometer to the weather station board, first have set up the main weather station box using the weather station guide.

1. Connect the anemometer to the wind vane
1. Connect the wind vane to the Raspberry Pi weather station

When connected the anemometer uses GPIO pin 5 (BCM)


## Sample Code

The following program uses a GPIO interupt handler to detect input from the anemometer, converting it to a speed in km/h. It also stores the last four speeds (20 seconds of readings) and checks for gust conditions:
- A wind speed above 29.6km/h in a 20 second period
- A variance in wind speed of 16.7km/h between the highest and lowest speed in that 20 second period

```python
from gpiozero import DigitalInputDevice
from time import sleep
import math

count = 0       # Counts how many half rotations
radius_cm = 9.0 # Radius of your anemometer
interval = 5    # How often (secs) to report speed
ADJUSTMENT = 1.18
CM_IN_A_KM = 100000.0
SECS_IN_AN_HOUR = 3600 
store_speeds = [] # Define a list to store last 4 wind speeds

# Every half rotation, add 1 to count
def spin():
    global count
    count = count + 1
    print( count )

# Calculate the wind speed given the time interval, the 
def calc_speed(time_sec):
        global count
        global store_speeds
        circumference_cm = (2 * math.pi) * radius_cm        
        rotations = count / 2.0

        # Calculate distance travelled by a cup in km
        dist_km = (circumference_cm * rotations) / CM_IN_A_KM

        # Speed = distance / time
        km_per_sec = dist_km / time_sec
        km_per_hour = km_per_sec * SECS_IN_AN_HOUR

        # Calculate speed
        final_speed = km_per_hour * ADJUSTMENT

        # Add this speed to the list
        store_speeds.append(final_speed)

        # If that takes the list over 4 items, chop off the first
        if len(store_speeds) > 4:
                store_speeds = store_speeds[1:]
      
        # Show what is in the store_speeds list
        print( str(store_speeds) )
        
        return final_speed

# Check whether the last 20 seconds of readings had any gusts
def check_for_gusts():
        highest = max(store_speeds)
        lowest = min(store_speeds)
        GUST_ABOVE = 29.6       
        GUST_RANGE = 16.7
        if highest > GUST_ABOVE and highest - lowest > GUST_RANGE:
                print("Gust! " + str(highest) + "km/h")        

wind_speed_sensor = DigitalInputDevice(5)
wind_speed_sensor.when_activated = spin


# Loop to measure wind speed and report at 5 second intervals
while True:
        count = 0
        sleep(interval)
        print( calc_speed(interval), "kph")
        check_for_gusts()

```

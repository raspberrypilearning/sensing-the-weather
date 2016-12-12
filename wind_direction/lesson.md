#  Sensing the Weather - Wind Direction Lesson

In this lesson students will learn how a more complicated sensor called a wind vane works. They will collect readings from the wind vane to determine the direction from which the wind is blowing.

## Sensor Guide

Background information about the [wind vane](about.md)

## Learning objectives

- Understand how the wind vane uses reed switches to change its output voltage
- Understand the difference between an analogue and a digital signal
- Be able to write a program to output the wind direction based on input from the wind vane

## Cross-Curricular applications

- Computer Science - instantiating objects, object methods
- Geography - wind direction for meteorological forecasts
- Mathematics - degrees, bearings, modulo operation
- Physics - resistance, circuits, analogue vs digital

## Lesson Summary

- Examine the wind vane and discuss its purpose, how it works and its units of measurement
- Review understanding of 360 degree angles (bearings) and compass points
- Discuss the concept of an object in a program
- Students code and test their wind direction program

## Starter

Examine the [wind vane](about.md) and discuss with pupils how it measures the wind direction. It is a much more complicated sensor than the rain gauge and anemometer sensors, still using reed switches but combining eight of these with variable resistors to alter the voltage output according to the position of the internal magnet. 

Recap the points of the compass and how these relate to bearings in degrees (a revision article on bearings can be found on [BBC Bitesize](http://www.bbc.co.uk/schools/gcsebitesize/maths/geometry/coordinatesandbearingsrev3.shtml)). 

## Main development

1. Set up the Raspberry Pi weather station and connect the wind vane. Turn the weather station on and log in.

1. This exercise makes use of a **class** someone else has written, a common occurrence in everyday programming. Students may already be familiar with using code from Python libraries such as `random` or `time`, this is exactly the same idea. It is important that your wind direction program is saved within the `weather_station` folder on the Raspberry Pi so that it can access the file containing this code, otherwise it will not work. Additionally, make sure that your code is **NOT** saved with the file name `wind_direction.py` as this is the name of the module you are trying to import. 

1. This code tells Python to get the contents of the `wind_direction` module, and when I refer to things from this module I want to refer to them by the name `wind_vane`. The reason we are using pre-written code here is because a lot of the necessary code to take readings from the ADC would be too complicated for students to write independently. 

1. You can use this opportunity to introduce students to the concept of **Object Oriented Programming**. We need to create an **object** which will allow us to gather readings from our wind vane.

	```python
	our_wind_vane = wind_vane.wind_direction(0, "wind_direction.json")
	```

	This code creates a variable `our_wind_vane` which is a pointer to a `wind_direction` object. (This is why we renamed the module to `wind_vane` earlier, otherwise we would have had to type `wind_direction.wind_direction` which is a bit confusing.) We have provided some necessary information to create the object - the ADC channel (0) and a config file (wind_direction.json).

1. Now we need to specify the interval to sample the wind direction in, and then get the direction:

	```python
	interval = 10
	print( our_wind_vane.get_value(interval) )
	```
	`get_value()` is a method which is called upon the `our_wind_vane` object. It contains code that returns a value in degrees for the direction of the wind vane. (You can examine this code if you want to, it is in the file `wind_direction.py` in the `weather_station` folder.)


1. Students work through the [worksheet](worksheet.md) to instantiate their wind vane object and take readings. They are challenged to display the compass direction the wind is blowing from, and to round the figures generated.

## Plenary

Ask the class the following questions:

- How is it possible for the wind vane to generate a direction in degrees?
- What is the difference between an analogue signal and a digital signal?

**Answers:**

- The degrees value comes from an average of voltage readings across the time interval chosen, in our case 10 seconds. These voltages are converted to degrees by code in the wind_direction library.
- The wind vane records a **range** of voltages, this is known as an *analogue* signal. Previous sensors simply reported a `HIGH` or `LOW` voltage - all or nothing. This is a *digital* signal.


## Extension

- The code inside the `wind_direction.py` module contains a function called `get_average()` which takes all angles read during the wind direction sampling interval and returns the average. Supposing there were three samples of 10&deg;, 20&deg; and 30&deg; and we took the mean average of these angles, we would get the result of 20&deg; which is correct:

```
(10 + 20 + 30) / 3 = 20
```
**Question:** Can students think of any problems with calculating the average in this way?

**Answer:** What if the angles reported were 355&deg;, 5&deg; and 15&deg; which would be a plausible fluctuation around North:

```
(355 + 5 + 15) / 3 = 125
```

...that's not right! To get the average calculated properly around a circle requires complicated code involving trigonometry, and is part of an area called Directional Statistics. This is far outside the scope of the classroom - hence why we used someone else's code to help us in this resource.
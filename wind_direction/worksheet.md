# Sensing the Weather - Wind Direction Worksheet

In this lesson you will:

- Understand how the wind vane uses reed switches to change its output voltage
- Understand the difference between an analogue and a digital signal
- Be able to write a program to output the wind direction based on input from the wind vane

## How does the wind vane work?

A wind vane shows the direction *from which* the wind is coming, not where it's going (this can be confusing because TV weather maps show the opposite). It works by the wind exerting force on a vertical blade which rotates to find the position of least resistance, this position is then aligned with the direction of the oncoming wind.

The wind vane is the more complex than the [rain gauge](../rainfall/about.md) or [anemometer](../wind_speed/about.md). It does use reed switches and magnets but it works in a completely different way. 

If you look inside the wind vane, you'll see there are eight reed switches arranged like the spokes of a wheel. 

![](images/wind_vane_reed.png)

So what is going on here? Firstly we need to understand what a [resistor](http://en.wikipedia.org/wiki/Resistor) is. These are small components that resist/reduce the flow of electrical current but do not stop it, at the same time they also reduce the voltage moving through the circuit. Resistors can have different values, a low resistance value would let almost all voltage/current through but a high resistance value would let very little through. As the magnet rotates different reed switches will open and close and thus switch their corresponding resistor in and out of the circuit.

Each of the 8 resistors have different values which you'll see printed in white text next to them, this then allows the wind vane to have 16 possible combinations of resistance since the magnet is able to close two reed switches when half way between them. More info in the [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf).


## Using the wind_direction code

firstly we need to import the module 

```python
import wind_direction as wind_vane
```

This code tells Python to get the contents of the `wind_direction` module, and when I refer to things from this module I want to refer to them by the name `wind_vane`. The reason we are using pre-written code here is because a lot of the necessary code to take readings from the ADC would be too complicated for students to write independently. 

1. Now is a good opportunity to introduce students to the concept of **Object Oriented Programming**. We need to create an **object** which will allow us to gather readings from our wind vane.

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

1. By placing this code inside a `while True:` infinite loop, we can repeatedly sample the wind direction. 

## Part 2 title

### Question
A question

### Answer
The answer

More instructions


Finished code

## Summary

- Questions to think about

## What's next

Ideas for things to do next
# Sensing the Weather - Wind Direction Worksheet

In this lesson you will:

- Bullet points

## How does the rain gauge work?

Brief description with pics


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
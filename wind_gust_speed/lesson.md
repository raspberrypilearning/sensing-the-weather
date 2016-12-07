#  Sensing the Weather - Wind Gust Speed Lesson

In this lesson students will learn how to use the anemometer to detect and store a range of wind speed values. The values from the previous 20 seconds will be evaluated to see if a gust of wind has occurred, and the gust speed will be recorded and displayed.

## Sensor Guide

Background information about using the [anemometer](about.md) to record gust speed

## Learning objectives

- To understand the definition of a 'gust of wind'
- To translate this definition into a format the computer can understand
- To be able to store wind speed measurements in a list for later analysis
- To be able to manipuate data items in a list

## Cross-Curricular applications

- Computer Science - lists, functions, constants, boolean logic, slicing 
- Geography - effects of gusts of wind, meteorological forecasting
- Mathematics - range, magnitude, max/min


## Lesson Summary

- What is a gust of wind?
- Storing generated data across a time period using a list
- Analysing data according to rules
- Testing a program

## Starter
Ask students "What is a gust of wind?" and discuss the answers received. Are any of them precise enough to be represented to the computer as instructions? We are going to use the anemometer to measure gusts of wind so we need a precise definition that a computer could check to decide whether it is true or false. 

Students could use the internet to research the meteorological definition of a gust of wind. The definition we have used can be found [here](http://glossary.ametsoc.org/wiki/Gust). (They may need to convert units to km/h, for example this page gives wind speed as knots rather than km/h.)

Ask them to devise a set of **specific** rules to be able to know when a gust of wind has occurred.

A gust occurs within a given time period when:
- the highest wind speed measured during that period is above 29.6km/h AND
- the difference between the peak speed and lowest speed in that period is greater than 16.7km/h AND
- the time period is 20 seconds or less


## Main development

1. Students boot the Raspberry Pi weather station with the anemometer attached (via the wind vane)
1. Make a copy of the `wind_final.py` code from the lesson on wind speed as we are going to adapt this to also show the current gust speed.
1. We want to record gusts over a time period of 20 seconds, so we will need to keep the most recent 4 speed readings from the anemometer. Introduce the concept of a list to store this data, and initialise a blank list with the other variables at the start of the program.

	```python
	store_speeds = []
	```
1. Students will also need to know how to do the following things to be able to piece together their program. You may want to teach these as concepts and then ask the students to write the program themselves, or you may wish to offer more help to guide them through the process of writing the program.

	### Add an item to a list

	```python
	item = 1.234
	store_speeds.append(item)
	```
	### Find the largest item in a list

	```python
	largest = max(store_speeds)
	```

	### Find the smallest item in a list

	```python
	smallest = min(store_speeds)
	```

	### Slice a section of the list

	The slicing operator takes a slice of the list in the following format:

	```python
	list_name[start:end]
	```
	So if we examine the following code:
	
	```python
	letters = ["a", "b", "c", "d", "e"]
	letters = letters[1:]
	```
	It is important to remember that list indexing begins at 0, so the 0th item in the list is "a", the 1st item is "b" and so on. The slicing starts at element 1 ("b") and there is no end point specified which means the slice will continue to the end of the list. The resulting sliced list will be `["b", "c", "d", "e"]` - we will have sliced off the first element.

	You can experiment with other slices, for example:

	```python
	letters = letters[2:4]
	```
	This would generate a list containing `["c", "d"]. This is because the slice starts at 2 (character `"c"`) and stops AT 4, but does not include item 4. Therefore we get the 2nd and 3rd items from the list.

1. Students follow the [worksheet](worksheet.md) to adapt their code to add gust speed monitoring.


## Plenary

Ask the class the following questions:

Questions here

**Answers:**

Answers here


## Extension

- Extension task

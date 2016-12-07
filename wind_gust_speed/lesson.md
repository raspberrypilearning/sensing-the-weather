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

- Computer Science - lists, functions, constants
- Geography - effects of gusts of wind, meteorological forecasting
- Mathematics - range, magnitude, max/min


## Lesson Summary

- What is a gust of wind?
- Storing generated data across a time period using a list
- Analysing data according to rules
- Testing a program

## Starter
Ask students "What is a gust of wind?" and discuss the answers received. Are any of them precise enough to be represented to the computer as instructions? We are going to use the anemometer to measure gusts of wind so we need a precise definition. Students could then use the internet to research the definition of a gust of wind. The definition we have used can be found [here](http://glossary.ametsoc.org/wiki/Gust). They may need to convert between speed units, for example this definition gives wind speeds as knots rather than km/h.

Ask them to devise a set of specific rules to be able to know when a gust of wind has occurred.

A gust occurs within a given time period when:
- the highest wind speed measured during a period is above 29.6km/h AND
- the difference between the peak speed and lowest speed in that period is greater than 16.7km/h AND
- the time period is 20 seconds or less


## Main development

1. Students boot the Raspberry Pi weather station with the anemometer attached (via the wind vane)
1. Make a copy of the `wind_final.py` code from the lesson on wind speed.


## Plenary

Ask the class the following questions:

Questions here

**Answers:**

Answers here


## Extension

- Extension task

#  Sensing the Weather - Barometric Pressure Lesson

In this lesson students will learn how to take readings from the barometric pressure sensor and to record this data in a CSV format for processing in another application.

## Sensor Guide

Background information about the [Barometric Pressure Sensor](about.md)

## Learning objectives

- Be able to take a reading from the barometric pressure sensor
- Understand what pressure is and the units it is measured in
- Be able to store data in a CSV format and access it from other applications

## Cross-Curricular applications

- Computer Science - writing to CSV, loops, concatenation, date and time functions
- Physics - mass, weight, pressure, Newtons, Pascals

## Lesson Summary

- Talk about what pressure is and how it is measured
- Introduce the Barometric Pressure sensor and write code to take a reading
- Students write code to read values from the sensor and write them to a CSV file

## Starter

Students may not be aware that air has a weight - introduce this concept and ask them how much they think a 1cm square cross section of air from sea level to the top level of the atmosphere would weigh. (The answer is approximately 10.1 Newtons, and the mass of the air is approximately 1.03kg.)

People often confuse mass with weight, largely because the activity involving scales that we describe as "weighing" should more accurately be described as "finding the mass"! Pressure is a measure of the *weight* (the force) relative to the *area* over which it is spread. There is a [BBC Bitesize](http://www.bbc.co.uk/education/guides/zssbgk7/revision) article you could use as a refresher.

The unit of pressure the weather station sensor measures in is called the **pascal** and it has the symbol Pa.

1Pa = 1 N/m<sup>2</sup>

## Main development

1. Students boot their Raspberry Pi weather station and log in. 

1. In order to read from the pressure sensor, the Adafruit BMP library must be installed. Open a terminal window and type in the following command to install the software: 

	```bash
	sudo pip3 install adafruit-bmp
	```

1. Here is some basic Python code which reads the current value from the barometric pressure sensor:

	```python
	import Adafruit_BMP.BMP085 as bmp

	bmpsensor = bmp.BMP085()

	print('Pressure = '+ str(bmpsensor.read_pressure()) + "Pa")
	```

1. Students type in the code and check that they can successfully take a reading. They will then follow the [worksheet](worksheet.md) instructions to take multiple readings and store these in a CSV file format.


## Plenary

Ask the class the following questions:

Questions here

**Answers:**

Answers here


## Extension

- Using the data you have gathered from the barometric pressure sensor, import the CSV file into another application and use that application to analyse the data. Perhaps you could import into Excel or Google Sheets and draw a graph of the pressure readings over time?

# Sensing the Weather - Barometric Pressure Worksheet

In this lesson you will:

- Be able to take a reading from the barometric pressure sensor
- Understand what pressure is and the units it is measured in
- Be able to store data in a CSV format and access it from other applications

## How does the barometric pressure sensor work?

Here is the barometric pressure sensor supplied with the Raspberry Pi Weather Station kit as part of the air board

![Barometric pressure sensor](images/pressure_sensor.png)

Our barometric pressure sensor measures pressure in Pascals (Pa). One Pascal is equal to one Newton per square metre.

1Pa = 1N/m<sup>2</sup>


## Taking a reading

1. Make sure that the Adafruit BMP library is installed on your weather station - ask your teacher how to do this if necessary. Here is the code to read the current pressure value from the sensor in Pa. Type in the code and check you can take a reading from the sensor:

	```python
	import Adafruit_BMP.BMP085 as bmp

	bmpsensor = bmp.BMP085()

	print('Pressure = '+ str(bmpsensor.read_pressure()) + "Pa")
	```

## Taking readings over time

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
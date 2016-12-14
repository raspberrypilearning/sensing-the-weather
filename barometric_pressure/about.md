# About the Barometric Pressure sensor

Here is the barometric pressure sensor supplied with the Raspberry Pi Weather Station kit as part of the air board

![Barometric pressure sensor](images/pressure_sensor.png)

The component is a BMP180 digital barometric pressure sensor.

## How does it work?

Barometric pressure is the pressure exerted by the weight of air. You might think that air does not weigh anything, but if you were to take a 1cm<sup>2</sup> cross section of air measured from sea level to the top level of the atmosphere, it would have a mass of approximately 1.03kg and weigh about 10.1 newtons. This air exerts a pressure of 101,000N/m<sup>2</sup>

Weight * Number of cm<sup>2</sup> in 1m<sup>2</sup> = Pressure in N/m<sup>2</sup>
**10.1N * 1000 = 101,000N/m<sup>2</sup>**

Our barometric pressure sensor measures pressure in millibars, so we need to know how to convert between the units of bars and Newtons/m<sup>2</sup>. The formula is as follows:

1 bar = 100,000 N/m<sup>2</sup> or
1 millibar = 100N/m<sup>2</sup>

Here is the [data sheet](https://www.rapidonline.com/pdf/35-1630_V1.pdf) for the BMP180 digital barometric pressure sensor.

## How does the sensor connect?

1. First, set up your main Raspberry Pi weather station box.
1. The barometric pressure sensor is a component on the air board. Connect the air board to the main weather station with the cable to the port labelled "Air Sensor".
1. Power on your weather station and log in.


## Sample Code

The following program detects blah
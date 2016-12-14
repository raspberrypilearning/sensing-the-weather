# About the Air Quality Sensor

Here is the Air Quality sensor supplied with the Raspberry Pi Weather Station kit, as part of the air board.

![Air Quality Sensor](images/air_quality_sensor.png)

## How does it work?

The air quality sensor detects the presence of contaminants in the air. The conductivity of the material inside the sensor increases depending on the concentration of detectable gases in the air around the sensor. This change in conductivity is converted to an output signal which corresponds to the gas concentration. The Python library converts this value into a percentage reading of hair purity, with 100% being completely free from detectable contaminants. 

This sensor is particularly sensitive to hydrogen, carbon monoxide and methane gases which are present in contaminants such as cigarette smoke and traffic fumes.

Here is the [data sheet](http://www.figarosensor.com/products/2600pdf.pdf) for the Air Quality Sensor.

## How does the sensor connect?

1. First, set up your main Raspberry Pi weather station box.
1. The air quality sensor is a component on the air board. Connect the air board to the main weather station with the cable to the port labelled "Air Sensor".
1. Power on your weather station and log in.


## Sample Code

The following program initialises an air quality sensor object and reads a value from it

```python
import tgs2600 as aqsensor

air_quality = aqsensor.TGS2600()

print( str(air_quality.get_value()) + "%")
```


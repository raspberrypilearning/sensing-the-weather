#  Sensing the Weather - Wind Speed Lesson

In this lesson students will learn how the anemometer works, use Python code to detect its rotation, and calculate the wind speed using a mathematical formula.


## Sensor Guide

Background information about [the anemometer](about.md)

## Learning objectives

- Understand how the anemometer works by triggering electrical signals each rotation
- Write code to count the signals produced by the anemometer and understand this data
- Write code to convert this raw data into wind speed information in a meaningful unit

## Cross-Curricular applications

- DT - designing an optimal method of attaching the anemometer to collect wind data
- Geography - wind speed data for local area
- Mathematics - circle theory
- Physics - reed switch sensor affecting voltage on a circuit

## Lesson Summary

- Examine the anemometer and discuss its purpose, how it works and its unit of measurement
- Review understanding of circle theory
- Discuss an algorithm for the anemometer program
- Students code and test the anemometer program
- Students calibrate their sensor to ensure accuracy

## Starter

Examine the anemometer sensor and discuss with pupils how it works and measures windspeed. (Review the [Anemometer Guide](about.md) for more detailed information.) Ask students what they think it does and how they think it works. Open it up and explore the sensor, reed switch and magnet as a group. Once you have explored how the sensor works as a group you should connect it up to a Raspberry Pi weather station in order to demonstrate later in the lesson.

Depending on time and ability of the class you may also want to recap some basic circle theory, including how to find the circumference of a circle. The [BBC Bitesize guide](http://www.bbc.co.uk/education/guides/z34xsbk/revision/2) has an explanation of the key formulae the students need and some questions to practice with. Students could be given a few questions where they find the circumference of a circle given the radius or diameter.

## Main development

1. Set up the Raspberry Pi weather station and connect the anemometer via the wind vane. Turn the weather station on and log in.

1. To be able to calculate wind speed, students will need to be able to count the signals coming from the anemometer. Remind students of the code from the previous lesson where we counted signals coming from the rain gauge:

   ```python
    from gpiozero import DigitalInputDevice

    rain_sensor = DigitalInputDevice(6)
    BUCKET_SIZE = 0.2794
    count = 0

    def bucket_tipped():
        global count
        count = count + 1
        print(count * BUCKET_SIZE)

    rain_sensor.when_activated = bucket_tipped
       
    ```

    Ask students how they would need to modify this code to gather data from the anemometer:

    - Change the device name from rain_sensor to wind_speed_sensor or similar
    - The anemometer is connected to GPIO pin 5, so change this too
    - We have no need for a bucket size so remove this in two places
    - Rename the function `bucket_tipped` to `spin` or similar
    
    
     Allow students time to adapt and test their code using the [student worksheet](worksheet.md). The code should display the number of **half** rotations counted. Press `Ctrl + C` to stop the program. The altered code should look like this:

    ```python
    from gpiozero import DigitalInputDevice

    wind_speed_sensor = DigitalInputDevice(5)
    count = 0

    def spin():
        global count
        count = count + 1
        print(count)

    wind_speed_sensor.when_activated = spin
       
    ```


1. Discuss with students how they will turn the count of signals received from the sensor into a wind speed. Share or co-devise with pupils an outline of code in a pseudocode style which students can refer to (there is an example in the [anemometer guide](about.md) Students should then implement the planned code in Python and test it.


## Plenary

Ask the class the following questions:

1. Why is calibration important?
1. Have we done enough to calibrate the anemometer?

**Answers:**

1. Because we want to be confident that our measurements are correct, or are at least within an acceptable tolerance.
1. The higher the wind speed, the less accurate the anemometer becomes. In order to compensate for this, we would need different calibration ratios for different speeds. With the information provided by the datasheet we have done as much as we can.


## Extension

- Students could test their anemometer with a fan or other wind source to ensure consistency.
- Students have used interrupts this lesson to collect inputs from the anemometer. Could they write a program to use continuous polling instead?
- Students could begin to think about the deployment of the weather station. Where would be an ideal location for the sensors? What factors might affect that decision? 


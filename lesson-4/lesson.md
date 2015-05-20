#  Weather Station Basic I/O - Lesson Plan 4

In this lesson, students will use the weather station expansion board and the anemometer (or simulate it). Students will learn how the anemometer works, use Python code to detect its rotation, and calculate the wind speed using a mathematical formula.

## Learning objectives

- To understand how the anemometer works by triggering electrical signals each rotation
- To count the signals produced by the anemometer and understand this data
- To convert this raw signal into meaningful information about the wind speed

## Learning outcomes

### All students are able to

- Explain how the anemometer works
- Write code (with help) to count the number of rotations made

### Most students are able to

- Write code to count the number of rotations made
- Use circle theory to convert the rotations made into a wind speed
- With support, present the wind speed in a meaningful unit

### Some students are able to

- Write code to gather anemometer data and calculate wind speed, and present this information in a suitable unit of measurement

## Lesson Summary

- Examine the anemometer and discuss its purpose, how it works and its unit of measurement
- Review understanding of circle theory
- Discuss an algorithm for the anemometer program
- Students code and test the anemometer program
- Students calibrate their sensor to ensure accuracy

## Starter

### How does the anemometer work?

Examine the anemometer sensor and discuss with pupils how it works and measures windspeed. Review the [Anemometer Guide](guides/weather_station/anemometer.md) for more detailed information.
- Ask students what they think it does and how they think it works.
- Open it up and explore the sensor, reed switch and magnet

Once you have explored how the sensor works you should connect it up to a Pi in order to demonstrate later in the lesson.

### Circle theory

Depending on your class you may also want to get them to recap some basic circle theory, including how to find the circumference of a circle. The [BBC Bitesize guide](http://www.bbc.co.uk/schools/gcsebitesize/maths/geometry/circlesrev2.shtml) has an explanation of the key formulae the students need and some questions to practice with. Students could be given a few questions where they find the circumference given the radius or diameter.

## Main development

Students largely follow the [worksheet]() and with some discussion points.
1. Students setup their Raspberry Pi and adapt their button setup and code to suit the anemometer.
2. Discuss with students how they will turn the count of signals received from the sensor into a wind speed.
	- Teacher led explanation
	- Class discussion
	- Share / co-devise with pupils a outline of code in a pseudocode style which students can refer to (example in [guide]())
3. Students to implement the planned code in python and test

## Plenary

Ask the class the following questions:

1. Why could we not use a pull down circuit to detect the anemometer spinning?
1. Why is calibration important?
1. Have we done enough to calibrate the anemometer?

**Answers:**

1. The weather expansion board has fixed circuitry that we cannot change. The rain gauge has two wires; one is hardwired to GPIO 17 and the other is hardwired to ground, which means we can only short GPIO 17 to ground. If we used a pull down on GPIO 17 we would be shorting ground to ground and this would not produce a detectable change in the `HIGH` or `LOW` state of GPIO 17 when the anemometer spins. It would only ever read `LOW`.
1. Because we want to be confident that our measurements are correct, or are at least within an acceptable tolerance.
1. We know that the higher the wind speed, the less accurate the anemometer becomes. In order to compensate for this, we would need different calibration ratios for different speeds. With the information provided by the datasheet we have done as much as we can.

## Extension

- Students could test their anemometer with a fan or other wind source to ensure consistency.
- Students have used interrupts this lesson to collect inputs from the anemometer. Could they write a program to use continuous polling instead?
- Students could begin to think about the deployment of the weather station. Where would be an ideal location for the sensors? What factors might affect that decision?

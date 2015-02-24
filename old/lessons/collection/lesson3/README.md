[Previous lesson](../lesson2/README.md)

# Lesson 3: The rain gauge

![](../../../images/rain_guage.jpg)

## Introduction

In this lesson students will use the weather station expansion board and the rain gauge. Students will firstly learn how the rain gauge works, then Python code will be written to interface with it, detect rainfall and display the measurement value.

## Resources

Students should work in pairs. Each pair will require the following equipment:

- Raspberry Pi
- Weather Station Expansion Board
- Rain gauge
- Micro USB power adaptor
- An SD Card with Raspbian already set up through NOOBS
- USB keyboard
- USB mouse
- HDMI cable
- A monitor or TV

## Learning Objectives

- Understand how the rain gauge works
- Understand how to write code to interface with it and produce a measurement
- Be able to differentiate between continuous polling and interrupt handler techniques
- Understand what de-bouncing is

## Starter



## Main Development



## Plenary

Ask the class the following questions.

1. Why we could not use a pull down circuit to detect the bucket tip?
1. Why is the unit of measurement for rainfall a length/depth as opposed to a volume?
1. What are the advantages of using interrupt handlers over continuous polling?
1. What is de-bouncing?

**Answers:**

1. The weather expansion board has fixed circuitry that we cannot change. The rain gauge has two wires; one is hard wired to GPIO 27 and the other is hard wired to ground. Which means we can only short GPIO 27 to ground. If we used a pull down on GPIO 27 we would be shorting ground to ground and this would not produce a detectable change in the `HIGH` or `LOW` state of GPIO 27 when the bucket tips. It would only ever read `LOW`.
1. The rain gauge measures only a small sample of the rain that falls from the sky, however we can generalise that the amount of rain falling into it will be the same as that falling everywhere locally per unit of surface area. This allows us to assert that our calculation of rainfall will equate to the amount of rain that has fallen over a much larger area than the rain gauge itself.
1. Interrupt handlers allow you to avoid having to write code to compare the current and previous states of the GPIO pin between each iteration of a continuous polling loop.
1. De-bouncing is a timeout, started when an interrupt occurs, during which subsequent interrupt events are ignored. This avoids switch bounce causing multiple, undesired, event detections that could produce erroneous results.

[Next lesson](../lesson4/README.md)

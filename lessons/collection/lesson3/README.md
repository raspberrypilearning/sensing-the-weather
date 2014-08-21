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

## Starter

Firstly ask everyone to remove the lid from their rain gauge. This is done by applying some pressure to the area of the case just above where the two screw holes are on the base. Squeeze gently here and the lid should pop off.

![](../../../images/rain_guage_open.jpg)

This rain gauge is basically a self emptying tipping bucket. Rain is collected by the lid and funnelled down into the bucket. Once enough rain water has collected gravity will make the bucket tip over, the water will drain out from the base, and the opposite bucket will come up into position.

So how do we interface with it? Let's consider what information we need in order to calculate a rainfall measurement.
- How much water will tip the bucket?
- How many bucket tips have happened?

If we know both of those the answer is easy: *Bucket volume multiplied by number of tips.*

The product [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf) tells us that 0.2794 mm of rain will tip the bucket. So we just need to know how many bicket tips have happened. To get that information we need to program the Raspberry Pi to detect when the bucket tips and keep a count.

Take a close look at the ridge between the two buckets. Inside this is a small cylindrical magnet that points towards the back wall. Inside the back wall there is a clever piece of electronics called a *reed switch*, pictured below.

![](../../../images/reed_switch.jpg)

The reed switch has two metal contacts inside it which will touch together when under the influence of a magnet. Therefore, electronically, this works in exactly the same way as the two jumper wires from the previous lesson. The code from the previous lesson will even work on it.

## Main Development

## Plenary



[Next lesson](../lesson4/README.md)

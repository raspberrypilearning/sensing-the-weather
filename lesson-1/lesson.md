# Weather Station Basic I/O - Lesson Plan 1


This lesson will introduce students to weather forecasting and how it works as well as some key weather terminology. Students will consider why gathering data about the weather is important and what data could be collected. They will be introduced to the Raspberry Pi weather station as a tool to automatically collect some of this data. It will also introduce the using a the Raspberry Pi GPIO pins to connect to measurement devices.

## Learning objectives

- To be familar with some key weather terminology
- To identify weather characteristics that can be measured, and understand how this is done
- To understand the potential use of the Raspberry Pi as an automated weather station
- To differentiate between the input and output modes of the GPIO interface and the terms `HIGH` and `LOW`

## Learning outcomes

### All students are able to

- Understand why collecting data is essential to weather forecasting
- Suggest a property of the weather that could be measured
- Explain the difference between input and output

### Most students are able to

- Suggest appropriate methods or devices for capturing weather data
- Understand that digital devices only read and produces two states `HIGH` / `LOW`

### Some students are able to

- Relate `HIGH` / `LOW` to other digital representations (ON/OFF, 1/0)
- Describe how the sensors might work and be able to connect to `HIGH` / `LOW` signals.

## Lesson Summary

- Decode a weather forecast.
- Consider what data needs to be captured?
- Introduce the Raspberry Pi and weather station sensors.
- What are the differences between input and output mode, what do `HIGH` & `LOW` mean?

## Starter

Begin by watching the video [How To... Decode A Weather Forecast](https://www.youtube.com/watch?v=lITCF3UPVu4) with the students quiz them afterwards on the meaning of some key vocab such as **high pressure**, **low pressure**, **fronts**, **isobars** etc.

Challenge students to suggest how meteorologists are able to make predications about the weather. Illicit the fact that they collect hugh amount of data to crete [forecast models](http://en.wikipedia.org/wiki/Weather_forecasting#How_models_create_forecasts)



## Main development

1. Get students to consider the different weather data that could be measured, and how this might be collected. This could be done through:
- general class discussion
- playing with the sensors and predicting what they might do
- a simple [cardsort](files/WeatherStationCardsort.pdf)

2. Introduce the Raspberry Pi and how we will use it to automatically collect data, student consider & discuss the benfits of the Raspberry Pi over a standard computer.

![](images/raspberrypis.png)
*The Raspberry Pi model B (left) and the B+ (right)*

This [Video](http://www.raspberrypi.org/help/what-is-a-raspberry-pi/) would  be useful at this point if pupils have never used a Raspberry Pi as would this [getting started lesson](http://www.raspberrypi.org/learning/getting-started-with-raspberry-pi-lesson/).

3. Focus on the General Purpose Input Output (GPIO) pins, students should understand that the pins can be connected to input or output devices. Students should identify some simple **input** and **output** devices. For each device students consider what it means when the voltage is `HIGH` or `LOW`.

## Plenary

Reiterate the meaning of HIGH and LOW by showing the voltage chart 

![](images/high_low.png)

Discuss with the class the following questions:

1. What would be happening if this graph was from the Output mode LED example?
1. What would be happening if this graph was from the Input mode button example?

*Answers:*

1. The LED is flashing on and off three times.
1. Someone is pressing and releasing the button three times.

## Extension

- Student's could consider how these digital signals might relate to the actual measurement of the weather. Eg What does High and Low mean in relation to the rain gauge?
- Are there any sensors for which the High / Low readings aren't clear or don't work? For example, how does the weather vane work, what is High and what is Low?

# Sensing the Weather - Rainfall Worksheet

In this lesson you will:

- Bullet points

## How does the rain gauge work?

Brief description with pics


## Getting Started

1. Set up your Raspberry Pi and ensure you are in desktop mode.

1. Launch the terminal

    ![Terminal](images/terminal.png)

1. Move to the `weather station` directory by typing `cd weather_station` and pressing `enter`

1. Make a copy of your rainfall_interrupt program to a new file called `wind_interrupt.py` by typing this command into the terminal and pressing enter

	```bash
	cp rainfall_interrupt.py wind_interrupt.py
	```

1. Open your program by typing `sudo idle3 wind_interrupt.py`

    The code will currently look like this:

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


## Part 2 title

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
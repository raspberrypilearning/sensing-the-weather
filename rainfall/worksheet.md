# Sensing the Weather - Rainfall Worksheet

In this lesson you will:

- Collect data using the Raspberry Pi Weather Station hardware
- Learn the difference between **continuous polling** and **interrupt handling**
- Convert the collected data into meaningful measurement information

## How does the rain gauge work?

Today you will be using the rain gauge sensor to collect data about rainfall. The gauge consists of a bucket to collect water, and a see-saw-like device to measure how much water passes through. Each time the bucket fills with a certain amount of water it tips, releasing the water and presenting the opposite bucket to be filled.

  ![](images/rain_gauge_both.jpg)

Each tip causes a magnet to pass in front a sensor called a reed switch, which closes the switch and triggers a `LOW` signal on GPIO pin 6. We can detect this `LOW` signal and use it to count how many times the bucket tips.

  ![](images/reed_switch.jpg)

In order to calculate the amount of water that has passed through the gauge we need to know:

  - The amount of water needed to tip the bucket, in this case **0.2794** mm (this can be found on the [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf)).
  - How many times the bucket has tipped, which can be counted as the number of input signals.

  `Rainfall = 0.2794 * number of tips`


## Counting bucket tips

Make sure your rain gauge is connected to your weather station, then turn it on.

1. Launch the terminal

  ![Terminal](images/terminal.png)


1. Move to the `weather station` directory by typing `cd weather_station` into the terminal and pressing `enter`

1. Start a new Python program by typing `sudo idle3 rain_polling.py`

1. We are going to set up the rain sensor as a digital input device - it is digital because when the bucket tips this causes a single input at a specific point in time rather than a gradual measurement of the bucket tipping.

We will also store the size of the bucket as a constant (hence the capitals) and a counter for how many times the bucket has tipped.

	 ```python
  from gpiozero import DigitalInputDevice

  rain_sensor = DigitalInputDevice(6)
  BUCKET_SIZE = 0.2794
  count = 0
	 ```

1. We want to count the number of times the bucket tips. Remember that when the bucket tips, this causes the reed switch to close and drops the voltage on GPIO pin 6 from `HIGH` to `LOW`. In order to do this, we need to keep track of the **current state** of the pin, the **previous state**, and the signal **count**. To do this, create three variables and set them each to 0.

	```python
	current_state = 0
	previous_state = 0
	```

1. The current state of the rain gauge sensor can be found by asking for the value. The value will be `True` if the GPIO pin has a `HIGH` voltage and `False` if it has a `LOW` voltage. 

```python
current_state = rain_sensor.value
```


1. We will want a `while True:` loop to constantly check the pin status, but we want to do something extra with it. In pseudocode (planning) our loop might look like this:


	> LOOP  
	> SET **CURRENT STATE** TO THE READING OF THE **SENSOR VALUE**  
	> IF **PREVIOUS STATE** = True AND THE **CURRENT STATE** = False THEN  
	> --- ADD 1 ONTO **COUNT**  
	> --- DISPLAY **RAINFALL**  
	> MOVE THE **CURRENT STATE** TO **PREVIOUS STATE**  
	> END LOOP  



  In Python we would write:

	```python
	while True:
	       current_state = rain_sensor.value

	        if previous_state == True and current_state == False:
	            count = count + 1
	            print ( count * BUCKET_SIZE )

			previous_state = current_state
	```

  You can see the complete code [here](code/rainfall_poll.py).

1. Once you have entered your code, run it by presing **F5**.
1. If you tilt the rain gauge a few times, your program should display something like:

    ```
    0.2794
    0.5588
    0.8382
    ```

1. You can quit at any time with the keystroke `CTRL + C`.

## Using interrupts in place of polling

So far we have used polling to repeatedly check the status of the input pin, which is very inefficient. The code constantly checks for rainfall every 0.01 seconds, which uses some processing power. Wouldn't it be better if the system only checked for rainfall when it was raining, and ignored the rain gauge the rest of the time?

To do that we need to use a technique called interrupt handling. Rather than constantly check the status of the pin, we use a mechanism called an interrupt to trigger a function.

1. From your rain_polling.py program in IDLE click the **file** menu and select **save as**, replace the file name with `rain_interrupt.py`

1. We need to make a few changes to the code: firstly, you should remove the variables **current_state** and **previous_state** as we won't need them.

1. Now, the code to increment the count and display the current rainfall needs to be moved into a function (a reusable section of code). You should call the function something sensible as you will need the name for the next step. We've called ours `bucket_tipped`. Here's what the first section of the code looks like now:

    ```python
    #!/usr/bin/python3
    import RPi.GPIO as GPIO

    pin = 6
    count = 0

    def bucket_tipped(channel):
        global count
        count = count + 1
        print(count * 0.2794)

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    ```

1. In order for your function to be triggered when the input voltage on pin 6 drops, you will need to define an interrupt event. Add this line to your code:

    ```python
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)
	```

    This line sets up the interrupt event on the `pin` and waits for a `GPIO.FALLING` event. When detected, it calls the `bucket_tipped` function. The `bouncetime=300` parameter specifies the minimum time, in milliseconds, between two events being detected.

1. Finally, we need a line to keep the program running, otherwise it will finish before any rain is detected. For now we'll get it to wait for the user to press `Enter`, and then exit.

    ```python
    input("Press Enter to stop logging\n")
	```

    The complete code can be found [here](code/rain_interrupt.py)

1. Run your code by pressing **F5**, this will ask you to save your code.
2. As you press your button you should see:

	```
	Press Enter to stop logging
	0.2794
	0.5588
	0.8382
	1.1176
	```
## Summary

You should now have a working rain gauge using two different approaches. Consider the following questions:

- What is the difference between polling and interrupt handling?
- Is one of these techniques better? If so, why?
- Why is the unit of measurement for the gauge **mm** rather than **ml**?

## What's next

Now that you have built your rain gauge code you should test its accuracy. How much water would 1mm be in the top of the bucket?

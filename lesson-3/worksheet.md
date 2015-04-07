# Weather Station Basic I/O - The Rain Gauge

In this lesson you will:

- Simulate a rain gauge and collect data using the Raspberry Pi GPIO pins
- Learn the difference between continuous polling and interrupt handling
- Convert the collected data into meaningful measurement information

## How does the rain gauge work?

1. Today you will be using the rain gauge sensor to collect data about rainfall. The gauge consists of a bucket to collect water and a see-saw-like device to measure how much water passes through. Each time the bucket fills with a certain amount of water it tips, releasing the water and presenting the opposite bucket to be filled.

  ![](images/rain_gauge_both.jpg)

1. Each tip causes a magnet to pass in front a sensor called a reed switch, which closes the switch and triggers a `LOW` signal on the GPIO pins. This is exactly the same as using a button or pair of wires, as done in the previous lesson.

  ![](images/reed_switch.jpg)

1. In order to calculate the amount of water that's passed through the gauge we need to know:

  - The amount of water needed to tip the bucket, in this case **0.2794** mm (this can be found on the [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf)).
  - How many times the bucket has tipped, which can be counted as the number of input signals.

  **Rainfall = 0.2794 * number of tips**

## What if I don't have a rain gauge?

In most classroom situations you won't have a rain gauge, or at least one to yourself, in which case you can simulate one using a pair of wires and a button.

1. Connect your wires up in a similar way to the previous lesson, except this time connect to pin 6.

	![](images/gpio-setup.png)
	
1. Now you can simulate a bucket tip with a simple press of the button.

## Counting bucket tips

1. You can reuse much of the code written last lesson to count the bucket tips. Set up your Raspberry Pi and enter the following command from the terminal:

	```bash
cp pullup.py rain_polling.py
	```
	
1. Next, edit the code with **nano**  by typing `nano rain_polling.py`.
1. In the top few lines change the pin being read to 6; the weather station is wired to use this pin so we should also use it for testing.

  ```python
  #!/usr/bin/python
  import RPi.GPIO as GPIO
  import time

  pin = 6

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    ```
    
1. We want to count the number of times the switch closes and drops the voltage from `HIGH` to `LOW`. In order to do this, we need to keep track of the **current state** of the pin, the **previous state**, and the signal **count**. To do this, create three variables and set them each to 0.

	```python
	current_state = 0
	previous_state = 0
	count = 0
	```

1. We will still want a `while True:` loop to constantly check the pin status, but we want to do something extra with it. In pseudocode (planning) our loop might look like this:
	
	
	> LOOP  
	> SET **CURRENT STATE** TO THE READING OF **INPUT PIN**  
	> IF **PREVIOUS STATE** = 1 AND THE **CURRENT STATE** = 0 THEN  
	> --- ADD 1 ONTO **COUNT**  
	> --- DISPLAY **RAINFALL**  
	> MOVE THE **CURRENT STATE** TO **PREVIOUS STATE**  
	> PAUSE 0.01 SECONDS  
	> END LOOP  
	

In Python we would write
		
	```python
	while True:
	       current_state = GPIO.input(pin)

	        if previous_state == GPIO.HIGH and current_state == GPIO.LOW:
	            count=count + 1
	            print (count * 0.2794)

			previous_state = current_state
	```
	
1. Once you have entered your code, you can save by pressing `CTRL + O` then `Enter`, and then exit with `CTRL + X`.
1. Ensure your code is executable by typing `chmod 755 rain_polling.py`.
1. Run your code with the command `sudo ./rain_polling.py`. If you press your button a few times, it should look something like this:

     ```
     pi@raspberrypi ~/weather_station $ sudo ./rain_polling.py 
0.2794
0.5588
	```
	
1. You can quit at any time with the keystroke `CTRL + C`. If your code doesn't work, review the steps and the complete `rain_polling.py` code [here](code/rain_polling.py).

## Using interrupts in place of polling

So far we have used polling to repeatedly check the status of the input pin, which is very inefficient. The code constantly checks for rainfall every 0.01 seconds, which uses some processing power. Wouldn't it be better if the system only checked for rainfall when it was raining, and ignored the rain gauge the rest of the time?

To do that we need to use a technique called interrupt handling. Rather than constantly check the status of the pin, we use a mechanism called an interrupt to trigger a function.

1. Copy your existing code to a new file called `rain_interrupt.py`:

	```bash
	cp rain_polling.py rain_interupt.py
	```
	
1. Open the code in nano to edit:

	```bash
	nano rain_interrupt.py
	```

1. The code to increment the count and display the current rainfall needs to be moved into a function. You should also remove the variables **current_state** and **previous_state** as we won't need them. You should call the function something sensible as you will need this function name for the next step. We've called ours `bucket_tipped`.

	```python
#!/usr/bin/python3
import RPi.GPIO as GPIO

pin = 6
count = 0

def bucket_tipped(channel):
    global count
    count = count + 1
    print (count * 0.2794)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

	```

1. In order for your function to be triggered when the input voltage on pin 27 drops, you will need to define an interrupt event. Add this line to your code:

	```python
GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)
	```

This line sets up the interrupt event on the `pin` and waits for a `GPIO.FALLING` event. When detected, it calls the `bucket_tipped` function. The `bouncetime=300` parameter specifies the minimum time, in milliseconds, between two events being detected.

1. Finally, we need a line to keep the program running, otherwise it will finish before any rain is detected. For now we'll get it to wait for the user to press `Enter`, and then exit.

	```python
input("Press Enter to stop logging\n")
	```

1. Save your code by pressing `CTRL + O` and `Enter`, then exit with `CTRL + X`.
1. From the terminal you should now be able to run your program by typing `sudo ./rain_interrupt.py`. The output should look something like this:

	```bash
pi@raspberrypi ~/weather_station $ sudo ./rain_interrupt.py
Press Enter to stop logging
0.2794
0.5588
0.8382
1.1176
	```

1. If your code doesn't work, check it against the full version [here](code/rain_interrupt.py).

1. You should now have a working rain gauge using two different approaches. Consider the following questions:

	- What is the difference between polling and interrupt handling?
	- Is one of these techniques better? If so, why?
	- Why is the unit of measurement for the gauge **mm** rather than **ml**?

## What's next

- Now that you have built your rain gauge code you should test its accuracy. How much water would 1mm be in the top of the bucket?

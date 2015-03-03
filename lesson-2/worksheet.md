# Lesson 2 - Capturing input signals

In this lesson you will:
1. Create and execute a prorgam to get the current state of Pin 4 and display it on screen.
2. Use a while loop to repeat nthis **polling** of the pin and output the result.
3. Add a delay to slow down the rate of **polling**.
4. Adapt the program to use a pull down circuit.
4. Explore the timings of the loop to get the ideal sensitivity.

## Reading an input pi

First we need to be able to make sure we can read the input pin 4, we will start by build a **pull up** circuit.

Connect your wires / buttons as shown:

![Pull up wires](images/pull_up_wire.png)

1. In LX terminal enter the command `nano pullup.py` and press Enter (nano is a text editor program).
1. Enter the code below.
  ```python
  #!/usr/bin/python3
  import RPi.GPIO as GPIO
  import time

  pin = 4

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

  pin_value = GPIO.input(pin)
  if pin_value == True:
    print ("HIGH")
  else:
    print()"LOW")
  ```

  **Code walkthrough:**

  | Code | Meaning |
  | --- | --- |
  |`#!/usr/bin/python3` | This line denotes this file as a Python program so that the computer knows *how* to run the code.|
  |`import RPi.GPIO as GPIO`<br>`import time`|  Imports the `RPi.GPIO` library that allows you to control the GPIO pins and the time library to measure time or make the program sleep.|
    |`pin = 4`<br>`GPIO.setmode(GPIO.BCM)`<br> `GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)`| These 3 lines setup a variable call pin to store the pin number. We then set the scheme for refering to our pins as the BCM scheme. The important bit is the 3rd line where we setup the pin as an input using a pull up resistor|
  |`pin_value = GPIO.input(pin)`| This line reads the state of the pin and stores the result in a variable called **pin_value**. This will either be *True* or *False*.|
  |`if pin_value == True:`<br>`print ("HIGH")`<br>`else:`<br>`print()"LOW")`|These lines check the value of the **pin_value** variable and prints out "HIGH" if the value is True and "LOW" if the value is False.|


1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. Next, mark the file as executable with the following command:

  `chmod +x pullup.py`
1. GPIO functions require root access on your Pi, so you must use the `sudo` command to run your code. If you don't use sudo you'll see the following error: `No access to dev/mem. Try running as root!`

  `sudo ./pullup.py`
1. The text `HIGH` should begin scrolling up the screen, when you hold the wires together (close the switch) for a few seconds you'll see the text `LOW` because you're shorting the pin to ground. Release the wires (open the switch) and it will return to `HIGH` because of the internal pull *up* resistor.

  ```
  HIGH
  HIGH
  HIGH
  HIGH
  LOW
  LOW
  LOW
  LOW
  HIGH
  HIGH
  HIGH
  HIGH
  ```
1. Press `Ctrl - C` to exit your program.

### Pull down circuit

1. Remove the jumper cables from the Raspberry Pi GPIO pins and reattach them as shown in the diagram below. Take care to select the correct pins.

  ![](images/pull_down_wire.png)

1. The code required to test the pull down circuit is almost identical to that for the pull up so to save time we will just make a copy of your file and change one thing. Enter the command below (this takes a copy of `pullup.py` and saves it as `pulldown.py`):

  `cp pullup.py pulldown.py`

1. Enter the command below to edit the new file:

  `nano pulldown.py`

1. Find the `GPIO.setup` line and change the last parameter from `GPIO.PUD_UP` to `GPIO.PUD_DOWN`. This sets the internal pull down resistor on GPIO 4 so that it will always read LOW. For example:

  `GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)`

1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. The file doesn't need to be marked as executable with `chmod` since this property was copied from the original file. You can go ahead and run your code now, remember to use `sudo`:

  `sudo ./pulldown.py`
1. The text `LOW` should begin scrolling up the screen, when you hold the wires together (close the switch) for a few seconds you'll see the text `HIGH` because you're shorting the pin to 3.3 volts. Release the wires (open the switch) and it will return to `LOW` because of the internal pull *down* resistor.

  ```
  LOW
  LOW
  LOW
  LOW
  HIGH
  HIGH
  HIGH
  HIGH
  LOW
  LOW
  LOW
  LOW
  ```
1. Press `Ctrl - C` to exit your program.

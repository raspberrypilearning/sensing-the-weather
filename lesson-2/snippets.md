







---
4. Run your pull_down code by pressing **F5** and see it working, what difference does a pull down circuit make?




Here we are going to use the internal pull up resistor to make GPIO 4 always read `HIGH`, then we will short it to ground through the wires so that it will read `LOW` when we touch the wires together.

*Note* : Pin numbers may be a little confusing at first, as there are a couple of numbering schemes which can be used. We will be using the **BCM scheme**. It may be worth having a pin reference sheet on the classroom wall or directing students to a guide such as [this](http://pi.gadgetoid.com/pinout). Some cases also have pin references on them.

Students should follow the worksheet to build their circuits and programs. There are a few points where you might wish to get the class to discuss what is happening.

The [worksheet](worksheet.md) follows these steps:

1. Create and execute a program to get the current state of pin 4 and display it on screen.
2. Use a `while` loop to repeat this **polling** of the pin and output the result.
3. Add a delay to slow down the rate of polling.
4. Adapt the program to use a pull down circuit.
4. Explore the timings of the loop to get the ideal sensitivity.
*****






Let's give it a try in practice.

## Reading an input pin

First we need to be able to make sure we can read the input from pin 4. We will start by building a **pull up** circuit.

Connect your wires / buttons as shown:

![Pull up wires](images/pull_up_wire.png)

1. Open LXTerminal from the menu bar:

  ![](images/lxterminal.png)

1. In LXTerminal, enter the command `nano pullup.py` and press Enter. 'nano' is a text editor program.
1. Enter the code below:

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



1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit nano.
1. Next, mark the file as executable with the following command:
`chmod +x pullup.py`

1. Type `sudo ./pullup.py` to test your code, ensuring that when the button is pressed you get the output `LOW` and `HIGH` if it is not pressed.

## Repeatedly polling the input pin

Currently, our code checks the pin status once and displays an appropriate output. Next, we are going to add a slight adaptation to make it check repeatedly or **poll** the pin.

1. Edit your code again. In LXTerminal enter the command `nano pullup.py` and press Enter.

1. You want to make the code simply check the pin over and over again until we stop the program. To do this we will wrap the main five lines of our program in a `while` loop. We will also add a pause to the program so that it doesn't check too often.

1. Adapt your code so that the last section looks like this (be careful to get the indentation correct):

  ```python
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

    while True:           #This line tells the program to loop the following indented section
        pin_value = GPIO.input(pin)
        if pin_value == True:
          print ("HIGH")
        else:
          print("LOW")
        time.sleep(0.5)   #This line adds a 0.5 second pause between polls.
  ```

1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit nano.
1. Enter `sudo ./pullup.py` to run your code.
1. The text `HIGH` should begin scrolling up the screen. When you hold the wires together (close the switch) for a few seconds, you'll see the text `LOW` because you're shorting the pin to ground. Release the wires (open the switch) and it will return to `HIGH` because of the internal pull *up* resistor.

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

## Adjusting polling time

Now that our code constantly polls the input pin for its state, we need to think about timing.

1. Can you press the button fast enough that the program misses it?

1. Experiment with the line `time.sleep(0.5)`. Change the time so that it always detects your input. Try different times and find the biggest pause that still detects the input.

## Pull down circuit

1. Remove the jumper cables from the Raspberry Pi GPIO pins and reattach them as shown in the diagram below. Take care to select the correct pins.

  ![](images/pull_down_wire.png)

1. The code required to test the pull down circuit is almost identical to that for the pull up, so to save time we will just make a copy of your file and change one thing. Enter the command below (this takes a copy of `pullup.py` and saves it as `pulldown.py`):

  `cp pullup.py pulldown.py`

1. Enter the command below to edit the new file:

  `nano pulldown.py`

1. There is one line in the program that needs updating to reflect the change from a **pull up** to a **pull down**. Which line is it?

1. Update the program and press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit nano.

1. The file doesn't need to be marked as executable with `chmod` since this property was copied from the original file. You can go ahead and run your code now, but remember to use `sudo`:

  `sudo ./pulldown.py`

1. The text `LOW` should begin scrolling up the screen. When you hold the wires together (close the switch) for a few seconds, you'll see the text `HIGH` because you're shorting the pin to 3.3 volts. Release the wires (open the switch) and it will return to `LOW` because of the internal pull *down* resistor.

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

## What's next?

In this lesson we have made our program respond to a single button press using a **pull up** and **pull down** setup.

- Are either of these circuits better than the other? Does it make a difference which one we use?
- In our code we used a button to print a simple statement. What else could you make it do?
- Could you connect multiple buttons to your Raspberry Pi and detect the states of each? Could you count the number of button presses?

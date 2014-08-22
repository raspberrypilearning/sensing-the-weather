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

The product [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf) tells us that 0.2794 mm of rain will tip the bucket. So we just need to know how many bucket tips have happened. To get that information we need to program the Raspberry Pi to detect when the bucket tips and keep a count.

Take a close look at the ridge between the two buckets. Inside this is a small cylindrical magnet that points towards the back wall. Inside the back wall there is a clever piece of electronics called a *reed switch*, pictured below.

![](../../../images/reed_switch.jpg)

The reed switch has two metal contacts inside it which will touch together when under the influence of a magnet. Therefore, electronically, this works in exactly the same way as the two jumper wires from the previous lesson. When the bucket tips the magnet passes the reed switch causing it to close momentarily. So we can use a *pull up* or *pull down* circuit to detect this, just like before.

The top of the back wall does come off if you want to see inside, just pull on the flat end gently and it should release. Inside there is a small circuit board that you can remove to examine. In the middle of it you will see the reed switch. Replace the circuit board and back wall lid before continuing. Leave the outer funnel/lid off for now.

## Main Development

### Setting up your Pi

1. Place the SD card into the slot of your Raspberry Pi.
1. Connect the Weather Expansion Board to the GPIO pins.
1. Connect the rain gauge to the socket marked *RAIN* on the Weather Expansion Board.
1. Next connect the HDMI cable from the monitor or TV.
1. Plug in the USB keyboard and mouse.
1. Plug in the micro USB power supply.
1. When prompted to login type:

    ```bash
    Login: pi
    Password: raspberry
    ```

### Run the code from lesson 2

1. Just as an experiment lets run the code from the previous lesson. Firstly we need to change the `pin` number in the code. Unlike the jumper wires from lesson 2 the weather expansion board is *fixed* circuitry that you cannot change. So we need to write our code to accommodate the way it's wired up. Enter the command below to edit `pullup.py` (remember nano is a text editor program):

  `nano pullup.py`

  The weather expansion board connects the rain gauge to GPIO 17 in a *pull up* circuit. So find the line where we define the `pin` variable and change the number 4 to 17. For example:
  
  `pin = 17`
  
1. This is all we need to change for now. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. Run the code and remember to use the `sudo` command:

  `sudo ./pullup.py`
  
1. The text `HIGH` should begin scrolling up. Hold the bucket in the middle position, exactly half way between the two tipping positions and you will see the text `LOW`.

### Improving the code

1. Of course holding the bucket like that is unrealistic, that would never happen during actual use. So try to simulate an actual bucket tip so that the magnet quickly passes the reed switch. A gentle tap of the upper bucket should be enough to drop it down. What do you see?

  Nothing? Try it a few times. If you're lucky, and you catch it at the right moment, you'll see maybe one `LOW`.

1. Press `Ctrl - C` to exit your program.
1. We have found a serious flaw in the code here. Remember inside the `while` loop there was the line `time.sleep(0.5)`? It takes a lot less than half a second for the magnet to flip past the reed switch. So we actually *miss* the event because our code was paused in the sleep function. We could reduce the sleep time causing the loop to run more often? Let's try this next.

  First copy the old code into a new file:

  `cp pullup.py rain_gauge.py`

  Edit the new file:

  `nano rain_gauge.py`

  Find the `time.sleep(0.5)` line and change 0.5 to 0.01. For example:
  
  `time.sleep(0.01)`
  
1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. Run the code and remember to use the `sudo` command:

  `sudo ./rain_gauge.py`

1. You'll notice the text scrolls up a *lot* faster this time, this is because the loop runs 100 times a second. Use your finger to flip the bucket and you should see at least a few lines of `LOW` scroll up and dissapear.
1. Press `Ctrl - C` to exit your program.
1. Now that the code is running fast enough to detect the bucket tip we also need to write some extra code to do the counting. We need to think about this carefully though. It's not as simple as keeping a count variable and adding one to it whenever the pin state is `LOW`. From the previous test you will have seen multiple `LOW` messages scroll up the screen when the bucket was tipped.

    What we need to do is only add one to the count when the pin state has changed from `HIGH` to `LOW` which should only occur *once* for every bucket tip (as the bucket tips it will go from `HIGH` to `LOW` and back to `HIGH`). To detect that we will need to know the pin state from the previous time around the loop so that we can compare it with the current pin state. So if the previous state was `HIGH` but this time its `LOW` we know the bucket has just tipped. Let's program this behaviour:
    
    `nano rain_gauge.py`

1. Change your code to match the code below:
    ```python
    #!/usr/bin/python
    import RPi.GPIO as GPIO
    import time
    
    pin = 17
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    
    count = 0
    current_state = 0
    previous_state = 0
    
    while True:
        current_state = GPIO.input(pin)
        
        if previous_state == GPIO.HIGH and current_state == GPIO.LOW:
            count += 1
            print count
        
        previous_state = current_state
        time.sleep(0.01)
    ```
  **Code walkthrough:**
  
  | Code | Meaning |
  | --- | --- |
  |`#!/usr/bin/python` | Denotes this file as a Python program.|
  |`import RPi.GPIO as GPIO` |  Imports the `RPi.GPIO` library.|
  |`import time` | Imports the `time` library.|
  |`pin = 17` | A reference variable to store the GPIO pin number connected to the rain gauge.|
  |`GPIO.setmode(GPIO.BCM)` | Sets the pin layout to match the diagrams that are part of this scheme of work.|
  |`GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)` | Enables internal pull up resistor so that the pin always reads HIGH.|
  |`count = 0` | Defines a variable that will be incremented by one when a bucket tip occurs.|
  |`current_state = 0` | A variable that will be used to store the current state of the GPIO pin for each iteration of the while loop.|
  |`previous_state = 0` | At the end of each loop iteration the current state will be copied into this variable so that it can be compared to the next current state.|
  |`while True:` | An infinite loop that must be manually aborted by the user. All lines of code that belong to this loop must be *indented*.|
  |`current_state = GPIO.input(pin)` | Reads the state of GPIO pin 17 and stores the result in the `current_state` variable.|
  |`if previous_state == GPIO.HIGH and current_state == GPIO.LOW:` | A Python *if* statement. An if statement tests the given condition, if true it will run the indented lines below, otherwise it skips over them. Here the condition is that the previous state equals `HIGH` *and* the current state equals `LOW`. Notice the double equal sign `==` is used to test for equality where as a single equal sign `=` is used for setting a variable.|
  |`count += 1` | Incrementing the `count` variable by one. Note that `+=` is a shorthand way to do `count = count + 1`.|
  |`print count` | Prints the contents of the `count` variable to the screen.|
  |`previous_state = current_state` | Copies the contents of the `current_state` variable into the `previous_state` variable so that it can be used by the if statement on the next iteration of the loop.|
  |`time.sleep(0.01)` | Pauses the execution of the code for 0.01 seconds.|

1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. Run the code and remember to use the sudo command:

  `sudo ./rain_gauge.py`

1. Dave
## Plenary

[Next lesson](../lesson4/README.md)

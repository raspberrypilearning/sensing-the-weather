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

Firstly ask everyone to remove the lid from their rain gauge. This is done by applying some pressure to the area of the case just above where the two screw holes are on the base. Squeeze gently here and the lid should pop off.

![](../../../images/rain_guage_open.jpg)

This rain gauge is basically a self emptying tipping bucket. Rain is collected by the lid and funnelled down into the bucket. Once enough rain water has collected gravity will make the bucket tip over, the water will drain out from the base, and the opposite bucket will come up into position.

So how do we interface with it? Let's consider what information we need in order to calculate a rainfall measurement.
- How much water will tip the bucket?
- How many bucket tips have happened?

If we know both of those the answer is easy: *Bucket volume multiplied by number of tips.*

The product [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf) tells us that 0.2794 mm of rain will tip the bucket. So we just need to know how many bucket tips have happened. To get that information we need to program the Raspberry Pi to detect when the bucket tips and keep a count.

If you look at the RJ11 plug on the end of the wire attached to the rain gauge you'll see there are only two wires inside, a red and a green one. Think of these as the two jumper wires from last time. Now take a close look at the ridge between the two buckets. Inside this is a small cylindrical magnet that points towards the back wall. Inside the back wall there is a clever piece of electronics called a *reed switch*, pictured below.

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
  |`GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)` | Enables internal pull up resistor so that pin 17 always reads HIGH.|
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
1. Run the code and remember to use the `sudo` command:

  `sudo ./rain_gauge.py`

1. Tip the bucket and you will see the number only displays *once* when you tip the bucket. This is a lot easier to read since we only use a print statement within the indented block of code that belongs to the if statement. Most of the time the evaluation of that if condition will be *false* and so the indented lines will be skipped.

  ```
  1
  2
  3
  4
  5
  ```

1. Press `Ctrl - C` to exit your program.
1. There is one thing left to do. Let's add the calculation to multiply the tip volume (0.2794) by the count. Enter the command below:

  `nano rain_gauge.py`

  Change the line `print count` to `print count * 0.2794`.
1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. Run the code and remember to use the `sudo` command:

  `sudo ./rain_gauge.py`

1. Tip the bucket a few times and now you'll see the actual measurement of rain in millimetres.

  ```
  0.2794
  0.5588
  0.8382
  1.1176
  1.397
  ```

1. Press `Ctrl - C` to exit your program.

### Using interrupt handling

The programming technique you have been using above is known as *continuous polling*. From the word *poll* meaning census, survey or ballot etc. Essentially the code keeps using the `GPIO.input` function, in a loop, to *poll* the state of the GPIO pin. To keep asking if it's `HIGH` or `LOW`. There is educational value in knowing how to program a pull up circuit in that way (which is why it's included here) however there is a much more efficient method that requires a lot less code.

It's called interrupt handling. Essentially we can just tell the computer that we want to be notified when a particular event happens, such as the GPIO pin going from `HIGH` to `LOW`, and the computer will raise an event that will cause some of our code to run. This eliminates the need for continuous polling and therefore the requirement to compare the current state to the previous state on each iteration of the loop.

1. Let's create a brand new file for this. Enter the command below:

    `nano rain_interrupt.py`

    Enter the code below:
  
    ```python
    #!/usr/bin/python
    import RPi.GPIO as GPIO
    
    pin = 17
    count = 0
    
    def bucket_tipped(channel):
        global count
        count += 1
        print count * 0.2794
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)
    
    raw_input("Press Enter to exit...")
    ```
    
  **Code walkthrough:**
  
  | Code | Meaning |
  | --- | --- |
  |`#!/usr/bin/python` | Denotes this file as a Python program.|
  |`import RPi.GPIO as GPIO` |  Imports the `RPi.GPIO` library.|
  |`pin = 17` | A reference variable to store the GPIO pin number connected to the rain gauge.|
  |`def bucket_tipped(channel):` | The `def` keyword is used to define your own functions. Here we define a function called `bucket_tipped`. Lines of code that belong to this function are indented. This will be the call back function that runs when a buck tip occurs. The function takes one parameter, `channel`, which is expected by the `RPi.GPIO` library.|
  |`global count` | This makes the `count` variable declared above available inside the scope of this function. Without this a new copy of the variable would be created locally just for this function and the main `count` variable would never change.|
  |`count += 1` | Incrementing the `count` variable by one. |
  |`print count * 0.2794` | Displays the calculation of tip volume multiplied by tip count.|
  |`GPIO.setmode(GPIO.BCM)` | Sets the pin layout to match the diagrams that are part of this scheme of work.|
  |`GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)` | Enables internal pull up resistor so that pin 17 always reads HIGH.|
  |`GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)` | This line is calling the `add_event_detect` function in the GPIO library to create the interrupt handler. This function takes four parameters. The GPIO pin number, the type of event (either `RISING`, `FALLING` or `BOTH`), the call back function and a bounce time in milliseconds. We pass in `FALLING` because it's a pull up circuit, when the pin is shorted to ground it goes from HIGH to LOW and therefore we want to detect the voltage `FALLING` from HIGH to LOW. The call back is the code we want to run when the interrupt occurs so here we pass in `bucket_tipped`. The bounce time is 300 milliseconds and this is used to avoid detecting multiple events in close succession that might occur if the bucket bounced back.|
  |`raw_input("Press Enter to exit...")` | The `raw_input` function is normally used to get text input from the user but here we are using it to hold up the program and prevent it from exiting. Pressing enter will release this function and cause the program to exit. |

1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. Because this is a new file we need to mark it as executable before we run it. Enter the command below:

  `chmod +x rain_interrupt.py`

1. Run the code and remember to use the `sudo` command:

  `sudo ./rain_interrupt.py`

1. Tip the bucket a few times and now you'll see the measurement of rain in millimetres just as before.

  ```
  0.2794
  0.5588
  0.8382
  1.1176
  1.397
  ```

1. Finally let's test the bounce time. This is designed avoid multiple event detections due to switch bounce. This happens with most buttons and switches and the technique is known as *de-bouncing*. If you flick the bucket down with some force you'll find that it bounces back to its original position. While the magnet actually passed the reed switch twice you'll notice that your program only detected *one* bucket tip. This is because the second tip occurred within 300 milliseconds of the first. 

1. Press Enter to exit your program.

## Plenary

Ask the class the following questions.

1. Why we could not use a pull down circuit to detect the bucket tip?
1. Why is the unit of measurement for rainfall a length/depth as opposed to a volume?
1. What are the advantages of using interrupt handlers over continuous polling?
1. What is de-bouncing?

**Answers:**

1. The weather expansion board has fixed circuitry that we cannot change. The rain gauge has two wires; one is hard wired to GPIO 17 and the other is hard wired to ground. Which means we can only short GPIO 17 to ground. If we used a pull down on GPIO 17 we would be shorting ground to ground and this would not produce a detectable change in the `HIGH` or `LOW` state of GPIO 17 when the bucket tips. It would only ever read `LOW`.
1. The rain gauge measures only a small sample of the rain that falls from the sky, however we can generalise that the amount of rain falling into it will be the same as that falling everywhere locally per unit of surface area. This allows us to assert that our calculation of rainfall will equate to the amount of rain that has fallen over a much larger area than the rain gauge itself.
1. Interrupt handlers allow you to avoid having to write code to compare the current and previous states of the GPIO pin between each iteration of a continuous polling loop.
1. De-bouncing is a timeout, started when an interrupt occurs, during which subsequent interrupt events are ignored. This avoids switch bounce causing multiple, undesired, event detections that could produce erroneous results.

[Next lesson](../lesson4/README.md)

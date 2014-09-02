[Previous lesson](../lesson3/README.md)

# Lesson 4: The anemometer

![](../../../images/anemometer.png)

## Introduction

In this lesson students will use the weather station expansion board and the anemometer. Students will firstly learn how the anemometer works, then Python code will be written to interface with it, detect its rotation and calculate the wind speed using a mathematical formula.

## Resources

Students should work in pairs. Each pair will require the following equipment:

- Raspberry Pi
- Weather Station Expansion Board
- Anemometer
- Micro USB power adaptor
- An SD Card with Raspbian already set up through NOOBS
- USB keyboard
- USB mouse
- HDMI cable
- A monitor or TV
- A small phillips screwdriver
- A ruler

## Learning Objectives

- Understand how the anemometer works
- Understand how to write code to interface with it and calculate wind speed

## Starter

Firstly ask everyone to pull the top off their anemometer, it goes back on just as easily. This is done by holding the base in one hand and pulling on the blades/cups with the other hand. It doesn't need much force to come off.

Look at the underside of the blades/cups and you'll see a small metal cylinder on one side. This is a magnet just like the one found on the bucket of the rain gauge. Test it with a paper clip if you like.

![](../../../images/anemometer_magnet.png)

Now use the screw driver to remove the three screws on the bottom of the base. The base should then pop out easily. Slide it down the cable about 10 to 20 cm to get it out of the way. Now if you look inside you'll see our old friend the reed switch again.

![](../../../images/anemometer_reed.png)

So what does this mean? When the blades/cups are in their original position and spinning the magnet will rotate in a tight circle above the reed switch. The magnet most influences the reed switch as it passes over the ends (where the gold wires come out). So for every complete rotation there will be two moments when the switch is closed.

So using a similar programming technique to the rain gauge we can count the number of interrupts and divide it by two to give us the number of complete rotations. We can then calculate the wind speed with some maths using π.

Reassemble the anemometer, put the base back into position and ensure the knot in the cable remains inside. Replace the three screws and push the blades/cups back onto the top. Give it a spin to check it rotates correctly.

## Main Development

### Setting up your Pi

1. Place the SD card into the slot of your Raspberry Pi.
1. Connect the Weather Expansion Board to the GPIO pins.
1. Connect the anemometer to the socket marked *WIND* on the Weather Expansion Board.
1. Next connect the HDMI cable from the monitor or TV.
1. Plug in the USB keyboard and mouse.
1. Plug in the micro USB power supply.
1. When prompted to login type:

    ```bash
    Login: pi
    Password: raspberry
    ```

### Detect the interrupts

1. We're going to carry on with interrupt detection from the previous lesson since this is more efficient than continuous polling. Remember the weather expansion board is *fixed* circuitry that you cannot change. So we need to write our code to accommodate the way it's wired up. The weather expansion board connects the anemometer to GPIO 27 in a *pull up* circuit (this is GPIO 21 on an old Rev 1 Raspberry Pi, a rev 1 board is easily [identifiable](../../../images/rev1pi.png) because it has no mounting holes).
1. Let's start a new program, enter the command below:

  `nano wind_speed.py`

1. Enter the code shown below:

    ```python
    #!/usr/bin/python
    import RPi.GPIO as GPIO
    
    pin = 27 #21 if using an old Rev 1 Raspberry Pi
    count = 0
    
    def spin(channel):
        global count
        count += 1
        print count
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=5)
    
    raw_input("Press Enter to exit...")
    ```

  **Code walkthrough:**
  
  | Code | Meaning |
  | --- | --- |
  |`#!/usr/bin/python` | Denotes this file as a Python program.|
  |`import RPi.GPIO as GPIO` |  Imports the `RPi.GPIO` library.|
  |`pin = 27` | A reference variable to store the GPIO pin number connected to the anemometer.|
  |`count = 0` | Defines a variable that will be incremented by one when the anemometer reed switch closes.|
  |`def spin(channel):` | The `def` keyword is used to define your own functions. Here we define a function called `spin`. Lines of code that belong to this function are indented. This will be the call back function that runs when the anemometer reed switch closes. The function takes one parameter, `channel`, which is expected by the `RPi.GPIO` library.|
  |`global count` | This makes the `count` variable declared above available inside the scope of this function. Without this a new copy of the variable would be created locally just for this function and the main `count` variable would never change.|
  |`count += 1` | Incrementing the `count` variable by one. |
  |`print count` | Displays the count.|
  |`GPIO.setmode(GPIO.BCM)` | Sets the pin layout to match the diagrams that are part of this scheme of work.|
  |`GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)` | Enables internal pull up resistor so that pin 27 always reads HIGH.|
  |`GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=5)` | This line is calling the `add_event_detect` function in the GPIO library to create the interrupt handler. This function takes four parameters. The GPIO pin number, the type of event (either `RISING`, `FALLING` or `BOTH`), the call back function and a bounce time in milliseconds. We pass in `FALLING` because it's a pull up circuit, when the pin is shorted to ground it goes from HIGH to LOW and therefore we want to detect the voltage `FALLING` from HIGH to LOW. The call back is the code we want to run when the interrupt occurs so here we pass in `spin`. The bounce time is only 5 milliseconds as opposed to 300 like last time. This is because we need to accommodate the anemometer spinning during high winds. A higher bounce time could cause desired counts to be ignored and we would be unable to calculate the wind speed correctly.|
  |`raw_input("Press Enter to exit...")` | The `raw_input` function is normally used to get text input from the user but here we are using it to hold up the program and prevent it from exiting. Pressing enter will release this function and cause the program to exit. |

1. Press `Ctrl - O` then `Enter` to save, followed by `Ctrl - X` to quit from nano.
1. Because this is a new file we need to mark it as executable before we run it. Enter the command below:

  `chmod +x wind_speed.py`

1. Run the code and remember to use the sudo command:

  `sudo ./wind_speed.py`

1. Hold the base of the anemometer in one hand and slowly rotate the blades/cups with the other. By doing this you can test that there are only ever *two* increments to the count for every complete rotation of the blades/cups. It can be helpful if you choose one cup and use it as a reference point for rotation.

  ```
  1
  2
  3
  4
  5
  6
  ```

1. Press `Enter` to exit your program.

### How to calculate wind speed

Ask the class to think back to their [geometry](http://www.bbc.co.uk/schools/gcsebitesize/maths/geometry/circlesrev1.shtml) maths lessons.

Our overall goal is to calculate the wind speed, or rather the speed at which the anemometer cups are spinning. Speed is a measurement of distance over time, for example: 20 kilometres *per hour*. So to calculate wind speed we need to measure how far the cups have travelled in a given block of time. Speed is then: distance ÷ time.

Since the cups rotate in circle we can use the anemometer circumference multiplied by the number of rotations to give us this distance. *It can be helpful to imagine wrapping a tape measure around your waist, if you then hold the tape out straight that is the circumference of your waist as a distance.* We already know that the number of rotations will be the `count` variable, in the above code, divided by two (because there are two interrupts per rotation).

![](../../../images/pi_diagram.png)

The number π is a mathematical constant that is the ratio of any circles circumference to its diameter. It's approximately 3.14159. Using π we can calculate the circumference of a circle if we know its diameter or radius. Take a ruler and measure the radius of the anemometer now. Measure from the small depression in the centre of the top to the very edge of one of the cups. You should find it's about 9 cm.

The formula to calculate circumference from radius is: **2πr**

So our maths to get the wind speed will be as follows:

- Count anemometer interrupts for time length **t**.
- Calculate anemometer circumference **c** with 2πr, radius r is 9 cm (c = 2 * π * 9).
- Calculate rotations **rt** by dividing `count` by two (rt = count / 2)
- Calculate total distance **d** by multiplying the circumference **c** by the rotations **rt** (d = c * rt)
- Calculate speed as total distance divided by time (speed = d / t)

### Units of measurement

When doing these kinds of calculations we must pay attention to the units of measurement used. The above example uses the radius in *cm* to calculate a circumference. So **c** will also be in *cm* and therefore so will the total distance **d**. Assuming the time **t** was in seconds our speed would then be in *cm per second*, not *km per hour*.

To be able to give the speed in km per hour we need to do two things:

- Convert either the radius or the total distance into kilometres before dividing by time. 

  There are 100 cms in a meter, and 1000 meters in a kilometre. So if you take a value in cm and divide it by 100,000 (100 * 1000) the answer is the distance in kilometres (or as a fraction of a kilometre).
- Convert speed as distance per second into distance per hour.

  There are 60 seconds in minute and 60 minutes in an hour, so if we multiply the distance per second by 3600 (60 * 60) we can convert to distance per hour.

### Program the calculation

1. Let's continue editing our program, enter the command below:

  `nano wind_speed.py`

1. Remember to add the new `import` line at the top. The `time` and `math` libraries are now needed. Change your code to match the code below:

    ```python
    #!/usr/bin/python
    import RPi.GPIO as GPIO
    import time, math
    
    pin = 27 #21 if using an old Rev 1 Raspberry Pi
    count = 0
    
    def calculate_speed(r_cm, time_sec):
        global count
        circ_cm = (2 * math.pi) * r_cm
        rot = count / 2
        dist_km = (circ_cm * rot) / 100000 # convert to kilometres
        km_per_sec = dist_km / time_sec
        km_per_hour = km_per_sec * 3600 # convert to distance per hour
        return km_per_hour
    
    def spin(channel):
        global count
        count += 1
        print count
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=5)
    
    interval = 5
    
    while True:
        count = 0
        time.sleep(interval)
        print calculate_speed(9.0, interval), "kph"
    ```

  **Code walkthrough:**
  
  | Code | Meaning |
  | --- | --- |
  |`#!/usr/bin/python` | Denotes this file as a Python program.|
  |`import RPi.GPIO as GPIO` |  Imports the `RPi.GPIO` library.|
  |`import time, math` | Imports both the `time` and `math` libraries. Multiple libraries can be imported on the same line with a comma to separate them.|
  |`pin = 27` | A reference variable to store the GPIO pin number connected to the anemometer.|
  |`count = 0` | Defines a variable that will be incremented by one when the anemometer reed switch closes.|
  |`def calculate_speed(r_cm, time_sec):` | Defining a function called `calculate_speed` to perform the wind speed calculation and return the answer. It will take two parameters: the radius, `r_cm`, and the time in seconds, `time_sec`, that we have been counting for.|
  |`global count` | This makes the `count` variable declared above available inside the scope of this function.|
  |`circ_cm = (2 * math.pi) * r_cm` | Calculates the circumference using the *2πr* calculation. When you see brackets around part of a calculation like this it is instructing the computer to perform that part *first*. So this is saying multiply π by two, get the answer and multiply *that* by `r_cm`.|
  |`rot = count / 2` | Calculates the number of full rotations. Simply divide the `count` of interrupts by two.|
  |`dist_km = (circ_cm * rot) / 100000` | Calculates the total distance. Note the use of brackets again. Multiply the circumference by the number of full rotations and then divide by 100,000 to get the answer in kilometres.|
  |`km_per_sec = dist_km / time_sec` | Calculate the speed per second. Divide the distance in kilometres by the time in seconds.|
  |`km_per_hour = km_per_sec * 3600` | Convert distance per second into distance per hour by multiplying by 3600.|
  |`return km_per_hour` | Returns the `km_per_hour` variable as the result of the function.|
  |`def spin(channel):` | This will be the call back function that runs when the anemometer reed switch closes.|
  |`global count` | This makes the `count` variable declared above available inside the scope of this function.|
  |`count += 1` | Incrementing the `count` variable by one. |
  |`print count` | Displays the count. You may wish to remove this to make the program output clearer.|
  |`GPIO.setmode(GPIO.BCM)` | Sets the pin layout to match the diagrams that are part of this scheme of work.|
  |`GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)` | Enables internal pull up resistor so that pin 27 always reads HIGH.|
  |`GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=5)` | Calling the `add_event_detect` function in the GPIO library to create the interrupt handler.|
  |`interval = 5` | This will be the time interval in seconds to count interrupts for before we attempt to calculate the speed.|
  |`while True:` | An infinite loop that must be manually aborted by the user.|
  |`count = 0` | On each iteration of this loop we should reset the interrupt count to zero, we want to see if the speed has gone up or down since last time so we need to discard the interrupt counts from the previous iteration.|
  |`time.sleep(interval)` | Pauses the execution of the code, in this loop only, for the number of seconds in the `interval` variable. Meanwhile the interrupt counting will continue in the background and the `count` variable will increase in value.|
  |`print calculate_speed(9.0, interval), "kph"` | Calls the `calculate_speed` function passing in the value 9.0 for the radius and `interval` for the time. The return value from `calculate_speed` is passed to the `print` command which shows it on screen along with the text `kph`.|

1. Press `Ctrl - O` then `Enter` to save, followed by `Ctrl - X` to quit from nano.

1. Run the code and remember to use the sudo command:

  `sudo ./wind_speed.py`

1. Start spinning the anemometer and every five seconds you should see a wind speed measurement display on the screen.

  ```
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  11
  12
  2.44290244743 km/h
  ```
  
  If you remove the `print count` line from the `spin` function the output will look a bit clearer.
  
1. This is usually where students like to compete to see who has the best pair of lungs. It's very easy to make yourself feel faint by doing this so make sure everyone is warned to not be standing up while blowing on the anemometer.

### Calibration



## Plenary

[Next lesson](../lesson5/README.md)

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
2. Let's start a new program, enter the command below:

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
  |`GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)` | Enables internal pull up resistor so that pin 17 always reads HIGH.|
  |`GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=5)` | This line is calling the `add_event_detect` function in the GPIO library to create the interrupt handler. This function takes four parameters. The GPIO pin number, the type of event (either `RISING`, `FALLING` or `BOTH`), the call back function and a bounce time in milliseconds. We pass in `FALLING` because it's a pull up circuit, when the pin is shorted to ground it goes from HIGH to LOW and therefore we want to detect the voltage `FALLING` from HIGH to LOW. The call back is the code we want to run when the interrupt occurs so here we pass in `spin`. The bounce time is only 5 milliseconds as opposed to 300 like last time. This is because we need to accommodate the anemometer spinning during very fast winds.|
  |`raw_input("Press Enter to exit...")` | The `raw_input` function is normally used to get text input from the user but here we are using it to hold up the program and prevent it from exiting. Pressing enter will release this function and cause the program to exit. |
  
## Plenary

[Next lesson](../lesson5/README.md)

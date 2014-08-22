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

  The weather expansion board connects the rain gauge to GPIO 17 in a *pull up* circuit. So find the line where we define the `pin` variable and change the number 4 to 17.
  
  `pin = 17`
  
2. This is all we need to change for now. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
3. Run the code and remember to the `sudo` command:

  `sudo ./pullup.py`
  
4. The text `HIGH` should begin scrolling up. Hold the bucket in the middle position, exactly half way between the two tipping positions and you will see the text `LOW`.

### Improving the code

1. Of course holding the bucket like that is unrealistic, that would never happen during actual use. So try to simulate an actual bucket tip so that the magnet quickly passes the reed switch. A gentle tap of the upper bucket should be enough to drop it down. What do you see?

  Nothing? Try it a few times. If you're lucky, and you catch it at the right moment, you'll see maybe one `LOW`.

2. Press `Ctrl - C` to exit your program. We have found a serious flaw in the code here. Remember inside the `while` loop there was the line `time.sleep(0.5)`? It takes a lot less than half a second for the magnet to flip past the reed switch. So we actually *miss* the event because our code was paused in the sleep function. There are two ways we can solve this, one is to reduce the sleep time causing the loop to run more often. Let's try this next:

  `nano pullup.py`

  Find the `time.sleep(0.5)` line and change 0.5 to 0.01.
  
  `time.sleep(0.01)`
  
3. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
4. Run the code and remember to the `sudo` command:

  `sudo ./pullup.py`

5. You'll notice the text scrolls up a *lot* faster this time, this is because the loop runs 100 times a second. Use your finger to flip the bucket and you should see at least a few lines of `LOW` scroll up and dissapear. Press `Ctrl - C` to exit your program.
6. Now that the code is running fast enough to detect the bucket tip we also need to write some extra code to count them.  

## Plenary

[Next lesson](../lesson4/README.md)

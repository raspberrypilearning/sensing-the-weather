[Previous lesson](../lesson4/README.md)

# Lesson 5: The wind vane

![](../../../images/wind_vane.png)

## Introduction

In this lesson students will use the weather station expansion board and the wind vane. Students will firstly learn how the wind vane works and understand the differences between analogue and digital signals. Python code will be written to convert the analogue signal from the wind vane to a digital number using an ADC (Analogue to Digital Converter). This number will then be used to determine the direction the wind vane is pointing.

## Resources

Students should work in pairs. Each pair will require the following equipment:

- Raspberry Pi
- Weather Station Expansion Board
- Wind vane
- Micro USB power adaptor
- An SD Card with Raspbian already set up through NOOBS
- USB keyboard
- USB mouse
- HDMI cable
- A monitor or TV
- A small phillips screwdriver (magnetic if possible)
- A print out of the [compass direction worksheet](Compass direction.pdf)

## Learning Objectives

- Understand how the wind vane works
- Be able to differentiate between analogue and digital signals
- Understand the purpose of an Analogue to Digital Converter
- Determine the direction of the wind vane

## Starter

A wind vane shows the direction *from which* the wind is coming, not where it's going (this can be confusing because TV weather maps show the opposite). It works by the wind exerting force on a vertical blade which rotates to find the position of least resistance, this position is then aligned with the direction of the oncoming wind.

Also known as a weather vane these are often found as decorative adornments at the highest point on buildings or churches. Typically taking the shape of a cockerel, horse or ship.

### How it works

The wind vane is the most complex of the sensors studied so far. It does use reed switches and magnets but it works in a completely different way. Ask the students to pull the top off their wind vane, it should come off without much force. On the underside you'll again find the metal cylinder which is the magnet.

![](../../../images/wind_vane_magnet.png)

*Note: Disassembling the next part is only recommended for students with good motor skills. Younger students may have difficulty reassembling it.*

Next take the screwdriver and remove the three screws in the base, slide the base panel down the cable a bit to get it out of the way. If you look inside now you'll see there are eight reed switches arranged like the spokes of a wheel. Remove the three remaining screws allowing the circuit board to come free. Do not lose these screws.

![](../../../images/wind_vane_reed.png)

Examine the green side of the circuit board now, this is the side that faces upward inside the wind vane. The magnet points down onto it. North is at the top in the picture above, where the two black clips for the anemometer socket are.

Look closely and you'll see there is a ring of metal that goes all the way around the edge. There is also a smaller ring in the centre. Each reed switch connects to the outer ring to the inner ring through a resistor. You'll see that `SW1` (switch 1) has `R1` near it (resistor 1), similarly `SW2` has `R2` and so on up to 8.

So what is going on here? Firstly students need to understand what a [resistor](http://en.wikipedia.org/wiki/Resistor) is. These are small components that resist/reduce the flow of electrical current but do not stop it, at the same time they also reduce the voltage moving through the circuit. Resistors can have different values, a low resistance value would let almost all voltage/current through but a high resistance value would let very little through.

The wind vane is working like a big variable resistor, think of a volume knob. Look at the schematic diagram below (a zigzag line is the symbol for a resistor). The idea is that voltage comes in on the outer ring and can take a path through any of the switches to the inner ring which is connected directly to ground. As the magnet rotates different reed switches will open and close and thus switch their corresponding resistor in and out of the circuit.

![](../../../images/wind_vane_schematic.png)

Each of the 8 resistors have different values which you'll see printed in white text next to them, this then allows the wind vane to have 16 possible combinations of resistance since the magnet is able to close two reed switches when half way between them. More info in the [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf).

Reassemble the wind vane now. Firstly locate the letter N on the side of the base, insert the circuit board with the green side facing away from you so that the anemometer socket aligns with North. Replace the three smaller screws (this step can be tricky and a magnetic screwdriver helps a lot). Next replace the base ensuring the knot in the cable remains inside. Finally replace the three larger screws.

### How can we measure it?

So we now understand that the wind vane is essentially a variable resistor similar to a volume knob (but with only 16 positions). Resistance is something that we can't measure directly because it's a passive property of the wind vane. What we need to do is measure something that changes as a *consequence* of the resistance. Namely the *voltage* going through the wind vane. The voltage level passing through it will go up and down as different resistors are switched on and off by the magnet. That, we *can* measure.

This is going to be entirely different to what we have done before. With the rain gauge and the anemometer we were working with voltage levels changing between 0 volts meaning *LOW* and 3.3 volts meaning *HIGH*. Our code could only tell us if a GPIO pin was HIGH or LOW but not somewhere in between. This is what is known as a *digital* signal, all or nothing, 1 or 0, HIGH or LOW. For the wind vane we need to accommodate a range between HIGH and LOW, this is known as an *analogue* signal.

### Analogue vs Digital

It is important for us to understand the general concept of analogue and digital. Think of a gaming control pad like the one below. The circle is highlighting the thumb joystick and the directional-pad. Ask the class which one is analogue and which one is digital?

![](../../../images/xbone_pad.png)

**Answers:**

- Thumb joystick: Analogue
  
  The thumb joystick is analogue because it provides a full range of motion between each direction. In a driving game you have the option to steer gently around a long sweeping corner or hard around a hairpin for example.

- Directional-pad: Digital

  The directional-pad is digital because the each direction button has only two states, on and off. Just like HIGH and LOW. In a driving game it would be like steering a car using the indicator stick, you would have full left and full right only. It would be very tricky to control!

Analogue and digital both have their place and often one works better for a particular task than the other. For a game like a flight simulator you would want analogue control to aim the plane, whereas for something simple like a jump, run and shoot platform game digital control is better.

### Analogue to Digital Conversion

So to recap then. The wind vane has a voltage going through it and this will vary according to which resistors are switched in and out by the reed switches and magnet. The challenge we face is being able to observe this analogue signal changing on a computer which is basically a digital machine.

![](../../../images/adc_msop10.png)

To do this we're going to use a clever microchip called an [Analogue to Digital Converter](http://en.wikipedia.org/wiki/Analog-to-digital_converter) or ADC for short. The weather expansion board has one of these built in (as do most games consoles). An ADC chip, like the one above, has a number of input pins. One of them is connected to the voltage going through the wind vane. We don't need to worry about the internal workings of the chip we just need to understand that it can convert from a continuous analogue voltage to a number (in code) that represents the voltage *magnitude*. More voltage will give a higher number, less voltage a lower one.

## Main Development

### Setting up your Pi

1. Place the SD card into the slot of your Raspberry Pi.
1. Connect the Weather Expansion Board to the GPIO pins.
1. Connect the wind vane to the socket marked *WIND* on the Weather Expansion Board.
1. Next connect the HDMI cable from the monitor or TV.
1. Plug in the USB keyboard and mouse.
1. Plug in an Ethernet cable for Internet access.
1. Plug in the micro USB power supply.
1. When prompted to login type:

    ```bash
    Login: pi
    Password: raspberry
    ```

### Install, configure and test

*Note: This will only need to be done once. But in a class environment it can help if this step has been done prior to starting the lesson.*

1. Before we can start we need to edit a few files, reboot and then install some software packages. We don't need to understand why or what this means. But, if you really want to know, this basically allows our code to talk to the [I²C](http://en.wikipedia.org/wiki/I%C2%B2C) microchips on the weather expansion board (such as the ADC chip). Enter the following at the command line:

  `sudo nano /etc/modprobe.d/raspi-blacklist.conf`

1. Comment out the line `blacklist i2c-bcm2708` by putting a `#` symbol at the start of the line.
1. Press `Ctrl - O` then `Enter` to save, followed by `Ctrl - X` to quit from nano.
1. Next set the I²C kernel module to automatically load at boot time:

  `sudo nano /etc/modules`

1. Type `i2c-dev` on a new line at the end of the file.
1. Press `Ctrl - O` then `Enter` to save, followed by `Ctrl - X` to quit from nano.
1. Reboot:

  `sudo reboot`

1. Login again as per usual. Next we need to download some library code which allows us to access the analogue to digital converter chip. Copy and paste the line below:

  `sudo wget https://raw.githubusercontent.com/raspberrypilearning/weather-station-sow/master/lessons/collection/lesson5/code/MCP342X.py --no-check-certificate`

  This will download a file called: `MCP342X.py` (MCP3427 is the name of the ADC chip by the way).

1. Let's test the library. Enter the commands below:
  ```bash
  chmod +x MCP342X.py
  sudo ./MCP342X.py
  ```
  The output should look *something* like this:
  ```
  CH0: 32767
  CH1: 32767
  ```
  If you see those two lines then everything is working correctly. Don't worry if the numbers are different.
  
  The `CH0` and `CH1` refers to the input *channels* on the ADC chip. Channel 0 is connected to the wind vane and channel 1 is connected to the Air Quality sensor (covered in a different lesson). So, for this lesson, we're only interested in channel 0.

### Detect wind vane rotation

1. Let's start a new program that will repeatedly display the value of channel 0 on the ADC. Enter the command below:

  `nano wind_direction.py`
  
1. Enter the code below:

  ```python
  #!/usr/bin/python
  import time
  from MCP342X import *
  
  adc = MCP342X()
  
  while True:
      print adc.read(0)
      time.sleep(0.1)
  ```
  **Code walkthrough:**
  
  | Code | Meaning |
  | --- | --- |
  |`#!/usr/bin/python` | Denotes this file as a Python program.|
  |`import time` | Imports the `time` library.|
  |`from MCP342X import *` | Imports the `MCP342X` library that allows us to talk to the ADC chip.|
  |`adc = MCP342X()` | This creates a special kind of variable called `adc` which is an [object](http://en.wikipedia.org/wiki/Object-oriented_programming). We can then use the Python syntax `adc.` to get access to the ADC functions.|
  |`while True:` | An infinite loop that must be manually aborted by the user. All lines of code that belong to this loop must be *indented*.|
  |`print adc.read(0)` | This prints the value of channel zero to the screen. It goes inside the `adc` object and calls the `read` function, passing in the channel number (which is zero). This instructs the ADC to take a reading from channel zero and return the answer, the value is then passed back to the `print` command which will display it on the screen.|
  |`time.sleep(0.1)` | Pauses the execution of the program so that the infinite loop doesn't overload the CPU.|
  
1. Press `Ctrl - O` then `Enter` to save, followed by `Ctrl - X` to quit from nano.
1. Mark your program as executable:

  `sudo chmod +x wind_direction.py`
  
1. Ensure that the wind vane is connected to the socket marked *WIND* on the weather expansion board.
1. Run the code and remember to use the `sudo` command:

  `sudo ./wind_direction.py`

1. Numbers should begin scrolling up the screen. Slowly rotate the wind vane in a complete circle but stop at each of the major directions for a few seconds at a time. 
  ```
  12926
  12926
  12926
  3981
  3981
  3981
  520
  520
  520
  ```
  You should find that the numbers remain semi-constant when you keep the wind vane still in one position. They may fluctuate up and down by one or maybe two. This is a phenomenon known as *jitter* and is something that all ADCs do.
  
1. So what do these numbers mean? As an experiment, leave your program running but disconnect the wind vane from the weather expansion board. You should now see the following output:
  ```
  32767
  32767
  32767
  32767
  32767
  ```
  This is the *maximum* number the ADC will give us. So these numbers represent the magnitude of the voltage going through the wind vane (it can range between 0 and 32767). Take another look at the wind vane diagram below. The ADC actually measures the voltage where the arrow is, just before it enters the wind vane. The wind vane circuit then siphons off some voltage to ground through the reed switches and resistors. That causes the voltage being measured by the ADC to *drop* in relation to which resistors are switched on by the magnet.
  
  ![](../../../images/wind_vane_schematic.png)
  
  If you completely disconnect the wind vane, like now, no voltage gets siphoned off to ground and so the full voltage is detected by the ADC and this is why we get the maximum value.

1. Reconnect the wind vane. Rotate it again to ensure the numbers are changing. You should see the same values as before ± 1 for a given direction. One other thing to note. As the numbers scroll up the screen, do you periodically see `32767` anyway?

  This is happening because the wind vane is not perfect and at some positions the magnet *doesn't close any reed switches*. This is the same as having the wind vane completely unplugged. The technical term for this is *open circuit* and we need to find a way to compensate for it in our code (more on this later).

1. Press `Ctrl - C` to stop the program.

### Translate into wind direction

So from our observations so far we can say the following:
  
- The number reported by the ADC is always the same (± 1) for a given direction.
- The numbers bear no relationship to the direction itself.
  
A volume knob doesn't seem like such a good comparison now. With a volume knob you would expect the readings to change in a linear way (this would cause the numbers reported by our code to increase and decrease proportionally to the rotation). The wind vane doesn't work like that, the resistors paired with each reed switch have seemingly been chosen randomly.

They have been chosen so that each direction just gives a *distinct* reading compared to all the others. As long as each direction gives us a different reading from the ADC we can work out what direction it is.
  
All we need to do is make our program *expect* the right numbers and translate them into the corresponding wind direction. It's also a sensible idea to represent the wind direction as a number as opposed to the traditional compass names (North, South etc). If we use a number we can then use code to easily compare wind directions and or work out an average.

Because there are 360 degrees in a circle it makes sense to use degrees clockwise from North. So 0° would be North, 90° would be East, 180° South and 270° West for example. So to recap there are going to be 16 possible wind directions that we can detect. There are only 8 reed switches but it's possible for the magnet to close two at the same time when half way between two (which gives us another 8 combinations).

1. Run the code again and remember to use the `sudo` command:

  `sudo ./wind_direction.py`
1. Complete the [compass direction worksheet](Compass direction.pdf) and record the ADC values for each direction.
1. Aim the wind vane at the chosen direction (remember the main four compass directions are embossed onto the plasic body). Then observe the ADC value repeating on the screen.
1. Write the number into the corresponding row of the worksheet. If the number is jittering just pick the most frequent one.
1. Do the shaded rows first, and only when you've recorded those attempt the white rows.
1. The white rows are for *half way* directions when two reed switches are closed by the magnet. These can sometimes be quite tricky to find, which is why it's good to have already recorded the value on either side so that you can clearly tell if you've found that sweet spot between the two. Sometimes it can help if you apply a little pressure to front of the rotary part as this makes the magnet go slightly closer to the reed switches. Don't be rough with it though, patience is a virtue.
1. Press `Ctrl - C` to stop the program when you have finished.

### Program the translation in code

1. Now we can program our code to take the number from the ADC and translate it into angle in degrees from north. Let's continue editing the code:

  `nano wind_direction.py`

  Do not take values from other people in the class. You will find that each wind vane may produce slightly different adc readings. Only use your own measurements in the code.

1. We're going to use a Python list to record our measurements. A typical list looks like this (don't type this in):

  `mylist = ['Cat', 'Dog', 'Parrot']`
  
  Square brackets `[]` are used to *enclose* a list and a comma `,` separates items *in* the list. Lists can also contain numbers:

  `mylist = [13, 14, 15]`
  
  Look again at your worksheet and you'll notice that, for each row, the degrees from north value increases by 22.5. This is because there are 16 directions that we can detect and (360 ÷ 16 = 22.5).
  
  Look at the **Row** column on your worksheet. If you multiply the row number by 22.5 you get the degrees from north. Try this on a calculator now.

1. Modify your code to match the code below. Note that `lookup_list` should contain the *ADC number* values from your worksheet. Replace the direction letters (N, NNE, NE etc) with the corresponding *ADC number* from your worksheet. Don't forget that each one must be followed by a comma except the last one.

  ```python
  #!/usr/bin/python
  import time
  from MCP342X import *
  
  lookup_list = [
  N,
  NNE,
  NE,
  ENE,
  E,
  ESE,
  SE,
  SSE,
  S,
  SSW,
  SW,
  WSW,
  W,
  WNW,
  NW,
  NNW ]
  
  def get_direction(adc_value, jitter_margin):
      found_pos = 0
      for loop_pos in range(len(lookup_list)):
          test_value = lookup_list[loop_pos]
          
          bottom_end = test_value - jitter_margin
          top_end = test_value + jitter_margin
          
          if adc_value >= bottom_end and adc_value <= top_end:
              found_pos = loop_pos
              break
      return found_pos * 22.5
  
  adc = MCP342X()
  
  while True:
      adc_value = adc.read(0)
      print get_direction(adc_value, 10)
      time.sleep(0.1)
  ```
1. Press `Ctrl - O` then `Enter` to save, followed by `Ctrl - X` to quit from nano.





## Plenary

[Next lesson](../lesson6/README.md)

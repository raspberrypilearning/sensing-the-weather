#  Weather Station Basic I/O - Lesson Plan 4

In this lesson students will use the weather station expansion board and the anemometer (or simulate it) . Students will discover learn how the anemometer works, then use Python code to detect its rotation and calculate the wind speed using a mathematical formula.

## Learning objectives

- Understanding how the anemometer works by triggering electrical siganals each rotation
- To count the signals produced by the anemometer and understand this is data.
- To convert this raw signal in to meaningful information about the wind speed.

## Learning outcomes

### All students are able to

- Explain how the anemometer works
- Write code (with help) to count the number of rotations made

### Most students are able to

- Write code to count the number of rotations made
- Use circle theorem to convert the rotations made into a wind speed.
- With support present the wind speed in a meaningful unit.

### Some students are able to

- Write code to gather anemometer data and calculate wind speed and present this information in a suitable unit of measurement.

## Lesson Summary

- Examine anemometer and discuss purpose, how it works and unit of measurement.
- Review understanding of Circle Theorem
- Discuss algorithm for anemometer program.
- Students code an test anemometer program.
- Students could calibrate their sensor to ensure accuracy

## Starter

### How does the anemometer work?
Show pupils the anemometer and ask them to consider:
- What does the device measure?
- How might it work?
- What unit of measure might it use?
- How would we capture data from this device in our code?

To help explain how the device works you can dismantle it following these steps:
1. First hold the base in one hand and pulling on the blades/cups with the other hand. It doesn't need much force to come off.

2. Look at the underside of the blades/cups and you'll see a small metal cylinder on one side. This is a magnet just like the one found on the bucket of the rain gauge. Test it with a paper clip if you like.

	![](images/anemometer_magnet.png)

3. Now use the screw driver to remove the three screws on the bottom of the base. The base should then pop out easily. Slide it down the cable about 10 to 20 cm to get it out of the way. Now if you look inside you'll see our old friend the reed switch again.

	![](images/anemometer_reed.png)

4. So what does this mean? When the blades/cups are in their original position and spinning the magnet will rotate in a tight circle above the reed switch. So for every complete rotation there will be two moments when the switch is closed.

5. So using a similar programming technique to the rain gauge we can count the number of interrupts and divide it by two to give us the number of complete rotations.

6. Reassemble the anemometer, put the base back into position and ensure the knot in the cable remains inside. Replace the three screws and push the blades/cups back onto the top. Give it a spin to check it rotates correctly.

### Circle Theory
Depending on your class you may also want to get them to recap some basic circle theory, including how to find the circumference of a circle. The [BBC Bitesize guide](http://www.bbc.co.uk/schools/gcsebitesize/maths/geometry/circlesrev2.shtml) has an explanation of the key formula the students need and some questions to practice with.

## Main development

### Setting up your Pi

1. Connect your pi up to the weather station add-on board and ensure the anemometer is connected to the weather station via the port marked "WIND".
2. Pupils are not likely to have their own weather station and so will have to connect their Pi to some wires or a button to simulate the weather station signal pulses.

![](images/gpio-setup.png)

### Detect the interrupts

Before starting practically, get students to open their rain gauge code and recap with the students what an **interrupt** is and why we might use them in place of **continuous polling**.

The first thing students need to do is adapt their rain_gauge code to make it gather data from the anemometer instead.

1. Copy the code from last lesson rain gauge and rename it as wind_speed.py.
	```bash
cp rain_interrupt.py wind_speed.py
```
2. Edit the code with nano
	```bash
nano wind_speed.py
```
3. There are 3 changes to be made.
- Firstly change the pin from 6 to 5
- Then change the name of the function from **bucket_tipped** to **spin**
- Remove the multiplier for rainfall and just print the count
- Finally change the function name in the event detection line to match the **spin** function

4. Their code should look like this:
	```python#!/usr/bin/python3
	import RPi.GPIO as GPIO

	pin = 5
	count = 0

	def spin(channel):
	    global count
	    count = count + 1
	    print (count)

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
	GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin, bouncetime=300)

	input("Press enter to stop logging\n")
	```

1. This will count the number of signals from the sensor and display the total on screen, there should be a signal detected each time the wires are connected (or for 1/2 a revolution).
2. Test the code by saving `Ctrl + O` , exiting `Ctrl + X` and then running:
	```bash
sudo ./wind_speed.py
```

### Calculate Wind Speed
After successfully testing the code the students need to convert the count variable into speed, discuss how this might be done with the students. Try to elicit the follow steps:

1. To calculate speed we need to use the formula
**Speed = Distance / Time**
2. **Time** is the easy bit as we can just decide how long to wait for before checking the number of signals detected, in our example we'll use 5 seconds.
3. **Distance** can be found from the number of signals counted by the code. each signal marks 1/2 a revolution which is equal to **π x r**
4. The radius can be measured as **9cm** which gives us a half rotation distance of **28.278cm**
5. So speed can be calculated by: **Speed = π x radius x count / 5**
6. This will give us a speed reading  in **cm per second**, we need to convert this to **km per hour**
7. FIrst we need to divide by 10000 to convert from **cm** to **km**
8. Then we need to convert from **seconds** to **hours** by multiplying by 3600

### Coding the solution
Give the students an outline solution in pseudocode / structured English or similar, for example:


> import GPIO,time,math  
> pin 5  
> count = 0  
>
> FUNCTION spin (channel)  
> --- increment global count varible  
> --- display count  
>
> FUNCTION calcspeed  
> --- using r = 9cm, t=5sec, count and math.pi  
> --- calulate windspeed in km / h  
> --- return windspeed  
>
> Setup GPIO and interrupt which has spin as it’s callback function.  
>
> LOOP  
> --- reset global count to 0  
> --- wait 5 sec  
> --- call calcspeed to get value  
> --- display windspeed value  


Ask the students to try code the solution using the above as a template, encourage students to collaborate, test and use trial and error to get there. A solution is provided here for reference:

```python
#!/usr/bin/python3
import RPi.GPIO as GPIO
import time, math

pin = 5
count = 0

def calculate_speed(r_cm, time_sec):
    global count
    circ_cm = (2 * math.pi) * r_cm
    rot = count / 2.0
    dist_km = (circ_cm * rot) / 100000.0 # convert to kilometres
    km_per_sec = dist_km / time_sec
    km_per_hour = km_per_sec * 3600 # convert to distance per hour
    return km_per_hour

def spin(channel):
    global count
    count += 1
    print (count)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
GPIO.add_event_detect(pin, GPIO.FALLING, callback=spin)

interval = 5

while True:
    count = 0
    time.sleep(interval)
    print (calculate_speed(9.0, interval), "kph")
```

At any point the students can run their code by exiting nano `Ctrl + O` followed by `Ctrl + X`, then typing `sudo ./wind_speed.py`.


### Calibration

Calibration is the practise of adjusting the value reported by a sensor to match a scientifically known value. In order to do this for the anemometer you would need a wind tunnel in your school where you could control the wind speed to an exact value. Since most of us don't have this available we'll need to make do.

Generally speaking anemometers tend to report the wind speed slightly lower than it actually is, a problem which gets progressively worse as the wind speed increases. Students can should follow the instructions in the worksheet to make a small adjustment to their reported value.

In order to get a more accurate reading the figure our program calculates needs to be multiplied by a factor of **1.18**. The final line of the `calculate_speed` function should now read :

```python
return km_per_hour * 1.18
```

Students should follow the instructions to implement this change and test the output of their code.

## Plenary

Ask the class the following questions.

1. Why we could not use a pull down circuit to detect the anemometer spinning?
1. Why is calibration important?
1. Have we done enough to calibrate the anemometer?

**Answers:**

1. The weather expansion board has fixed circuitry that we cannot change. The rain gauge has two wires; one is hard wired to GPIO 17 and the other is hard wired to ground. Which means we can only short GPIO 17 to ground. If we used a pull down on GPIO 17 we would be shorting ground to ground and this would not produce a detectable change in the `HIGH` or `LOW` state of GPIO 17 when the anemometer spins. It would only ever read `LOW`.
1. Because we want to have confidence that our measurements are correct (or are at least within an acceptable tolerance).
1. We know that the higher the wind speed the further from correct the anemometer becomes. In order to compensate for this we would need different calibration ratios for different speeds. With the information provided by the datasheet we have done as much as we can.

## Extension

- Students could test their anemometer with a fan or other wind source to ensure consistency.
- Students have used interrupts this lesson to collect inputs from the anemometer, could they write a program to use continuous polling instead.
- Students could begin to think about the deployment of the weather station, where would be an ideal location for the sensors. What factors might affect that decision?

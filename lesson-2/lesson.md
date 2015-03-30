# Weather Station - Data Collection Lesson Plan 2 - Using GPIO input mode

In this lesson students will experiment with the Raspberry Pi GPIO and do some Python programming. We are going to focus on input mode specifically since this is more appropriate to sensing things from the outside world than output mode. This knowledge will be used to interface with the rain gauge and wind speed sensors in later lessons.

## Learning objectives

- Understand what a pull up circuit is, what a pull down circuit is and be able to differentiate the two
- Understand how to detect the position of a switch in the Python programming language
- To gain practical experience in programming and electronics

## Learning outcomes

### All students are able to

- Write a short piece of Python code to capture to input of a sensor.
- Use a while loop and pause to repeat this capture of data.

### Most students are able to

- Write code to use both a **pull up** and **pull down** circuit.
- Be able to explain what each of these circuits do

### Some students are able to

- Experiment with timings and decide how often to capture data from the sensor.

## Lesson Summary

- Connect a basic switch and discuss pull_up / pull_down circuits.
- Capture data from the GPIO Pin (using pull_up circuit).
- Add a loop and timings
- Adapt to create a pull_down circut
- Explore to get the timings right

## Starter

In this lesson we are going to make a very basic switch and program the Raspberry Pi to detect its position. The switch will could actually just be two jumper wires that you touch together, or it could be a button if you have them. If they are touching the switch is closed, if not the switch is open.

![](images/jumpers.jpg)

In the previous lesson we learnt about HIGH and LOW. In order to detect the open and closed position in code the switch must turn voltage on and off for a GPIO pin. Then, using input mode, we can detect a change in the pin's value in our code.

When a GPIO pin is in input mode the pin is said to be *floating*, meaning that it has no fixed voltage level. That's no good for what we want, as the pin will randomly float between HIGH and LOW. We need to categorically know that the wires have touched. So we need to fix the voltage level to HIGH or LOW, and then make it change *only* when the we touch the wires together.

We can do this in two ways:

- A [pull up circuit](images/pull_up.png) pulls the voltage up to 3.3 volts and reads as HIGH by default. When the buttton is pressed the voltage drops to LOW.

- A [pull down circuit](images/pull_up.png) pulls the voltage down to 0 volts and reads as LOW by default. When the buttton is pressed the voltage jumps to HIGH.

Fortunately, the Raspberry Pi has all the above circuitry built in. It can be helpful to imagine that the two resistors `R1` and `R2` from the diagrams above are *inside* the circuitry of the Raspberry Pi and they can be enabled or disabled as we desire. We can select either a pull up or a pull down *in our code* for each GPIO pin.

Let's give it a try in practice next.

## Main development

1. We will test our switch in both pull up and pull down circuit configurations. First students [connect and boot](http://www.raspberrypi.org/help/quick-start-guide/) their Raspberry Pi and load LX Terminal

### Pull up circuit

Here we are going to use the internal pull up resistor to make GPIO 4 always read HIGH, then we will short it to ground through the wires so that it will read LOW when we touch the wires together.

*Note : Pin numbers may be a little confusing at first, it may be worth have a pin reference sheet on the classroom wall. Some cases also have pin reference on them. Also The first 26 pins on a B+ are the same as those on a model A or B.*

Students follow the worksheet to build their circuits and their programs, there are a few points at which you might wish to focus the class to discuss what is happening.

The [worksheet](worksheet.md) follows these steps:
1. Create and execute a prorgam to get the current state of Pin 4 and display it on screen.
2. Use a while loop to repeat this **polling** of the pin and output the result.
3. Add a delay to slow down the rate of **polling**.
4. Adapt the program to use a pull down circuit.
4. Explore the timings of the loop to get the ideal sensitivity.


## Plenary

Show this table to the class to recap. It is important to recognise that the pull up and pull down circuits give opposite values when the switch is open and closed. It can help if you first cover up the pull down column, and then cover up the pull up column instead.

Pull up | Switch | Pull down
:---:|:---:|:---:
HIGH | Open | LOW
HIGH | Open | LOW
HIGH | Open | LOW
HIGH | Open | LOW
LOW | Closed | HIGH
LOW | Closed | HIGH
LOW | Closed | HIGH
LOW | Closed | HIGH
HIGH | Open | LOW
HIGH | Open | LOW
HIGH | Open | LOW
HIGH | Open | LOW

Ask the class the following questions.

1. Explain why the pull up shows those values.
1. Explain why the pull down shows those values.
1. Is one circuit better than the other? If so why?
1. We've learnt an important technique in this lesson which will allow us to interface with two of the weather station sensors. Which sensors we will use this for?

**Answers:**

1. With a pull up circuit the GPIO pin is internally pulled up to 3.3 volts (via a programmable resistor) so that it always reads HIGH. When we close the switch we short the GPIO pin to ground causing it to read LOW.
1. With a pull down circuit the GPIO pin is internally pulled down to ground (via a programmable resistor) so that it always reads LOW. When we close the switch we short the GPIO pin to 3.3 volts causing it to read HIGH.
1. Neither is better, they are both an equally valid way to detect a switch or push button.
1.  The rain guage and the anemometer (wind speed sensor).
up

## Extension

- Somethingdsa
- Something else

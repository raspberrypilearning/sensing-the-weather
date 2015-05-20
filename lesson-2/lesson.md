# Weather Station Basic I/O - Lesson Plan 2

In this lesson students will experiment with the Raspberry Pi GPIO pins and do some Python programming. We are going to focus on input mode specifically, since this is more appropriate to sensing things from the outside world than output mode. This knowledge will be used to connect with the rain gauge and wind speed sensors in later lessons.

## Learning objectives

- Understand what pull up and pull down circuits are, and be able to differentiate between the two
- Understand how to detect the state of a switch from within the Python programming language
- Write a Python program which includes an infinite loop to check the state of the switch

## Learning outcomes

### All students are able to

- Write a short piece of Python code to capture the input of a sensor
- Use a `while` loop and pauses to repeat this capture of data

### Most students are able to

- Write code to use both a pull up and pull down circuit
- Explain what each of these circuits do

### Some students are able to

- Experiment with timings and decide how often to capture data from the sensor

## Lesson Summary

- Connect a basic switch and discuss pull up and pull down circuits
- Capture data from a GPIO pin using a pull up circuit
- Add a loop and timings
- Adapt to create a pull down circut
- Explore to get the timings right

## Starter

Use the [Pull Up/Pull Down Guide](guides/GPIO/pull_up_down.md) to explain the different ways in which an input signal can be detected by the Raspberry Pi. This could be done through:
- Teacher-led explanation
- Role play
- Analogy

## Main development

1. Students follow [Pull Up/Pull Down Guide](guides/GPIO/pull_up_down.md) to connect a button to the Raspberry Pi.
2. Students refer to lesson [worksheet](worksheet.md) to write a python program to read an input pin in a pull up circuit.
3. Students add a loop to their code to make it poll continuously and report the status of the pin.
4. Students adapt their program to use a Pull Down resistor setup instead of a Pull Up.


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

Discuss the following with the class:

1. Explain why the pull up shows those values.
1. Explain why the pull down shows those values.
1. We've learnt an important technique in this lesson which will allow us to interface with two of the weather station sensors. Which sensors we will use this for?

**Answers:**

1. With a pull up circuit the GPIO pin is internally pulled up to 3.3 volts (via a programmable resistor) so that it always reads `HIGH`. When we close the switch we short the GPIO pin to ground, causing it to read `LOW`.
1. With a pull down circuit the GPIO pin is internally pulled down to ground (via a programmable resistor) so that it always reads `LOW`. When we close the switch we short the GPIO pin to 3.3 volts, causing it to read `HIGH`.
1.  The rain gauge and the anemometer (wind speed sensor).

## Extension

Students could consider the following ideas and questions:

- Is either one of these circuits better than the other? Does it make a difference which one we use?
- In our code we used a button to print a simple statement, but what else could you make it do?
- Could you connect multiple buttons to your Raspberry Pi and detect the states of each? Could you count the number of button presses?

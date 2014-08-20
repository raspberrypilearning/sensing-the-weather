[Previous lesson](../lesson1/README.md)

# Lesson 2: Using GPIO input mode

## Introduction

In this lesson students will experiment with the Raspberry Pi GPIO and do some Python programming. We are going to focus on input mode specifically since this is more appropriate to sensing things from the outside world than output mode.

## Resources

Students should work in pairs and will each pair need the following equipment:

- Raspberry Pi
- Micro USB power adaptor
- An SD Card with Raspbian already set up through NOOBS
- USB keyboard
- USB mouse
- HDMI cable
- A monitor or TV
- Two **Male to Female** jumper wires (try [Pimoroni](http://shop.pimoroni.com/products/jumper-jerky))

## Learning Objectives

## Starter

In this lesson we are going to make a very basic switch and program the Raspberry Pi to detect its position. The switch will actually just be two jumper wires that you touch together. If they are touching the switch is closed, if not the switch is open.

In the previous lesson we learnt about the HIGH and LOW states of GPIO pin. In order to detect the open or closed position in code the switch must turn voltage on and off for a GPIO pin. Then, using input mode, we can detect a change in the HIGH/LOW value in code.

When a GPIO pin is in input mode the pin is said to be *floating*, meaning that it has no fixed voltage level. That's no good for what we want, as the pin will randomly float between HIGH and LOW. We need to categorically know that the wires have touched. So we need to fix the voltage level to HIGH or LOW, and then make it change *only* when the we touch the wires.

We can do this in two ways:

- A pull up circuit

  Wire the GPIO pin to 3.3 volts through a large 10kΩ resistor so that it always reads HIGH. Then we can short the pin to ground by touching the wires, so that the pin will go LOW.

  ![](../../../images/pull_up.png)

- A pull down circuit

  Wire the GPIO pin to ground through a large 10kΩ resistor so that it always reads LOW. Then we can short the pin to 3.3 volts by touching the wires, so that it goes HIGH. When the wires touch there is a lower resistance path to 3.3 volts, and therefore the pin will read HIGH. 

  ![](../../../images/pull_down.png)
  
  *Note: The 1kΩ R2 resistor is there in both circuits to give the GPIO pin a fail-safe protection, in case we mistakenly set the pin to be in OUTPUT mode.*


## Main Development

## Plenary

[Next lesson](../lesson3/README.md)

[Previous lesson](../lesson1/README.md)

# Lesson 2: Using GPIO input mode

## Introduction

In this lesson students will experiment with the Raspberry Pi GPIO and do some Python programming. We are going to focus on input mode specifically since this is more appropriate to sensing things from the outside world than output mode. This knowledge will be used to interface with the rain gauge and wind speed sensors in later lessons.

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

In this lesson we are going to make a very basic switch and program the Raspberry Pi to detect its position. The switch will actually just be two jumper wires that you touch together, see below. If they are touching the switch is closed, if not the switch is open.

![](../../../images/jumpers.jpg)

In the previous lesson we learnt about HIGH and LOW. In order to detect the open and closed position in code the switch must turn voltage on and off for a GPIO pin. Then, using input mode, we can detect a change in the pin's value in our code.

When a GPIO pin is in input mode the pin is said to be *floating*, meaning that it has no fixed voltage level. That's no good for what we want, as the pin will randomly float between HIGH and LOW. We need to categorically know that the wires have touched. So we need to fix the voltage level to HIGH or LOW, and then make it change *only* when the we touch the wires together.

We can do this in two ways:

- A pull up circuit

  Wire the GPIO pin to 3.3 volts through a large 10kΩ resistor so that it always reads HIGH. Then we can short the pin to ground by touching the wires together so that the pin will go LOW.

  ![](../../../images/pull_up.png)

- A pull down circuit

  Wire the GPIO pin to ground through a large 10kΩ resistor so that it always reads LOW. Then we can short the pin to 3.3 volts by touching the wires together so that it goes HIGH. When the wires touch there is a lower resistance path to 3.3 volts, and therefore the pin will read HIGH. 

  ![](../../../images/pull_down.png)
  
  *Note: The 1kΩ R2 resistor is there in both circuits to give the GPIO pin a fail-safe protection, in case we mistakenly set the pin to be in OUTPUT mode.*

Fortunately, the Raspberry Pi has all the above circuitry *built in* and we can select either a pull up or a pull down circuit *in our code* for each GPIO pin. Let's give it a try in practice next.

## Main Development

We will test our switch in both pull up and pull down circuit configurations.

### Setting up your Pi

1. Place the SD card into the slot of your Raspberry Pi.
1. Next connect the HDMI cable from the monitor or TV.
1. Plug in the USB keyboard and mouse.
1. Plug in the micro USB power supply.
1. When prompted to login type:

    ```bash
    Login: pi
    Password: raspberry
    ```

### Pull up circuit

Here we are going to use the internal pull up resistor to make GPIO 4 always read HIGH, then we will short it to ground through the wires so that it will read LOW when we touch the wires together.

*Note: The first 26 pins on a B+ are the same as those on a model A or B.*

1. Attach the female ends of the jumper wires to the Raspberry Pi GPIO pins as shown below. Take care to select the correct pins.

  ![](../../../images/pull_up_wire.png)

2. Go to the Linux command prompt, either Exit the desktop or open LX Terminal.
3. Enter the command `nano pullup.py` and press Enter.
4. Enter the code below.
  ```python
  #!/usr/bin/python
  import RPi.GPIO as GPIO
  import time
  
  pin = 4
  
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
  
  while True:
      pin_value = GPIO.input(pin)
      print pin_value
      time.sleep(0.5)
  ```
  **Code walkthrough:**
  
  The first line ` #!/usr/bin/python` denotes this file as a Python program so that the computer knows *how* to run the code. All of your Python programs will have this.
  
  The next two `import` lines give you access to some pre-written libraries of code. The first `RPi.GPIO as GPIO` allows you to control the GPIO pins. The second one `time` allows you to measure time or make the program sleep.
  
  We then define a variable called `pin` and store the value 4 in it. This will be used whenever you need to refer to the GPIO pin number that you're using later on in the program.
  
  Wherever you see the syntax `SOMETHING.` the *dot* signifies accessing a function or properly inside the thing before the dot. So `GPIO.setmode` is going inside the `GPIO` library and calling the function `setmode`. This configures the pin layout that you want to use. The brackets `()` are important because they enclose the function *parameters;* the input data that the funciton needs. You can input either `GPIO.BCM` or `GPIO.BOARD` to this function. We're going to use `GPIO.BCM` here since layout this matches the diagrams that are part of this resource. `GPIO.BOARD` sets the pin numbers up in a sequential fashion and some programmers prefer it that way. If you prefer to use `GPIO.BOARD` then the `pin` variable should be changed from 4 to 7.
  
  The next line `GPIO.setup` configures the IO (input/output) mode for a given GPIO pin. When you want to input multiple parameters to a function you separate them with a comma `,`. There are three parameters; `pin` which specifies the number of the GPIO pin to configure; `GPIO.IN` specifies that we want to use input mode and `GPIO.PUD_UP` is saying we want to turn on the internal pull up resistor so that the pin always reads HIGH.
  
  Now everything is set up and we can start reading the pin value. To keep it simple the program will just use a loop to repeat the same set of instructions. Those instructions will read the value of GPIO 4 and display it on the screen allowing you to see the pin value changing in real time. We're going to use a *while* loop. A while loop is usually used with a condition such as `while a < b` (while a is less than b) meaning that the looping will carry on as long as that condition remains true. So if *a* becomes equal to or greater than *b* the loop would exit.
  
  The `while True` syntax specifies an infinite loop. The keyword `True` is a *constant* (not a variable) and so the loop will never exit unless we press `Ctrl - C`. It's not the most elegant way to program it but this is just test code after all.
  
  Whenever you see a colon `:` think of this as meaning *then*. So while True *then repeat these lines of code*. The subsequent lines are indented to denote that they all belong to the loop. You can either use multiple space characters or a tab character for indentation. If you prefer to use spaces then the number of spaces in the indentation can be variable, as long as they remain constant in each block of code. **Understanding the rules of indentation is fundamental to Python; it can be a stumbling block for pupils.** Pupils often do not understand what white space is; they therefore need to be shown that spaces and tabs are real text characters which are normally invisible in text editors. It can also be helpful to offer a quick demonstration in Microsoft Word where some code is typed out and the paragraph toolbar button is used to show the hidden characters. Space characters then show as a dot and tab characters show as an arrow.
  
  
  
  
5. Dave

### Pull down circuit

## Plenary

[Next lesson](../lesson3/README.md)

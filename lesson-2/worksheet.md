# Lesson 2 - Capturing input signals

In this lesson you will:
1. Create and execute a prorgam to get the current state of Pin 4 and display it on screen.
2. Use a while loop to repeat nthis **polling** of the pin and output the result.
3. Add a delay to slow down the rate of **polling**.
4. Adapt the program to use a pull down circuit.
4. Explore the timings of the loop to get the ideal sensitivity.

## Reading an input pi

First we need to be able to make sure we can read the input pin 4, we will start by build a **pull up** circuit.

Connect your wires / buttons as shown:

![Pull up wires](images/pull_up_wire.png)

1. In LX terminal enter the command `nano pullup.py` and press Enter (nano is a text editor program).
1. Enter the code below.
  ```python
  #!/usr/bin/python3
  import RPi.GPIO as GPIO
  import time

  pin = 4

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

  pin_value = GPIO.input(pin)
  if pin_value == True:
    print ("HIGH")
  else:
    print()"LOW")
  ```

  **Code walkthrough:**

  | Code | Meaning |
  | --- | --- |
  |`#!/usr/bin/python3` | This line denotes this file as a Python program so that the computer knows *how* to run the code. All of your Python programs will have this.|
  |`import RPi.GPIO as GPIO` |  Imports the `RPi.GPIO` library that allows you to control the GPIO pins.|
  |`import time` | Imports the `time` library that allows you to measure time or make the program sleep.|
  |`pin = 4` | A variable called `pin` to store the number 4. This will be used whenever you need to refer to the GPIO pin number that you're switching voltage on and off for later on in the program.|
  |`GPIO.setmode(GPIO.BCM)` | Wherever you see the syntax `SOMETHING.` the *dot* signifies accessing a function or properly inside the thing before the dot. So `GPIO.setmode` is going inside the `GPIO` library and calling the function `setmode`. This configures the pin layout that you want to use. The brackets `()` are important because they enclose the function *parameters;* the input data that the funciton needs. You can input either `GPIO.BCM` or `GPIO.BOARD` to this function. We're going to use `GPIO.BCM` here since this layout matches the diagrams that are part of this lesson. `GPIO.BOARD` sets the pin numbers up in a sequential fashion and some programmers prefer it that way. If you prefer to use `GPIO.BOARD` then the `pin` variable should be changed from 4 to 7.|
  |`GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)` | This configures the IO (input/output) mode for a given GPIO pin. When you want to input multiple parameters to a function you separate them with a comma `,`. There are three parameters; `pin` which specifies the number of the GPIO pin to configure; `GPIO.IN` specifies that we want to use input mode and `GPIO.PUD_UP` is saying we want to turn on the internal pull up resistor so that the pin always reads HIGH.|
  |*Note:*|Now everything is set up and we can start reading the pin value. To keep it simple the program will just use a loop to repeat the same set of instructions. Those instructions will read the value of GPIO 4 and display it on the screen allowing you to see the pin value changing in real time. We're going to use a *while* loop. A while loop is usually used with a condition such as `while a < b` (while a is less than b) meaning that the looping will carry on as long as that condition remains true. So if *a* becomes equal to or greater than *b* the loop would exit.|
  |`while True:`| The `while True` syntax specifies an infinite loop. The keyword `True` is a *constant* (not a variable) and so the loop will never exit unless we press `Ctrl - C`. It's not the most elegant way to program it but this is just test code after all.|
  |*Note:*|Whenever you see a colon `:` think of this as meaning *then*. So `while True:` *while true is true then repeat these lines of code*. The subsequent lines are indented to denote that they all belong to the loop. You can either use multiple space characters or a tab character for indentation. If you prefer to use spaces then the number of spaces in the indentation can be variable, as long as they remain constant in each block of code. **Understanding the rules of indentation is fundamental to Python; it can be a stumbling block for students.** Students often do not understand what white space is; they therefore need to be shown that spaces and tabs are real text characters which are normally invisible in text editors.|
  |`pin_value = GPIO.input(pin)`| This is defining a variable called `pin_value` and setting it to the result of the `GPIO.input` function. This will go and get the value of the specified GPIO pin number (based on the voltage going into it) so we pass the variable `pin` in as a parameter. The result value will be either `1` if HIGH or `0` if LOW.|
  |`print "HIGH" if pin_value else "LOW"`| This line uses a `print` statement with an in-line `if` statement. It will print the text HIGH if `pin_value` is `1` otherwise it will print LOW.|
  |`time.sleep(0.5)`| This line uses a function inside the `time` library called `sleep`, the function accepts only one parameter which is how long you want it to sleep for. Here we specify half a second. This essentially pauses the execution of the code for half a second on each iteration of the loop.|

1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. Next, mark the file as executable with the following command:

  `chmod +x pullup.py`
1. GPIO functions require root access on your Pi, so you must use the `sudo` command to run your code. If you don't use sudo you'll see the following error: `No access to dev/mem. Try running as root!`

  `sudo ./pullup.py`
1. The text `HIGH` should begin scrolling up the screen, when you hold the wires together (close the switch) for a few seconds you'll see the text `LOW` because you're shorting the pin to ground. Release the wires (open the switch) and it will return to `HIGH` because of the internal pull *up* resistor.

  ```
  HIGH
  HIGH
  HIGH
  HIGH
  LOW
  LOW
  LOW
  LOW
  HIGH
  HIGH
  HIGH
  HIGH
  ```
1. Press `Ctrl - C` to exit your program.

### Pull down circuit

1. Remove the jumper cables from the Raspberry Pi GPIO pins and reattach them as shown in the diagram below. Take care to select the correct pins.

  ![](images/pull_down_wire.png)

1. The code required to test the pull down circuit is almost identical to that for the pull up so to save time we will just make a copy of your file and change one thing. Enter the command below (this takes a copy of `pullup.py` and saves it as `pulldown.py`):

  `cp pullup.py pulldown.py`

1. Enter the command below to edit the new file:

  `nano pulldown.py`

1. Find the `GPIO.setup` line and change the last parameter from `GPIO.PUD_UP` to `GPIO.PUD_DOWN`. This sets the internal pull down resistor on GPIO 4 so that it will always read LOW. For example:

  `GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)`

1. Press `Ctrl - O` then Enter to save, followed by `Ctrl - X` to quit from nano.
1. The file doesn't need to be marked as executable with `chmod` since this property was copied from the original file. You can go ahead and run your code now, remember to use `sudo`:

  `sudo ./pulldown.py`
1. The text `LOW` should begin scrolling up the screen, when you hold the wires together (close the switch) for a few seconds you'll see the text `HIGH` because you're shorting the pin to 3.3 volts. Release the wires (open the switch) and it will return to `LOW` because of the internal pull *down* resistor.

  ```
  LOW
  LOW
  LOW
  LOW
  HIGH
  HIGH
  HIGH
  HIGH
  LOW
  LOW
  LOW
  LOW
  ```
1. Press `Ctrl - C` to exit your program.

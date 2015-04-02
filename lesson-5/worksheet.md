# Weather Station Basic I/O - Combining our code

In this lesson you will:

- Review the code for the anemometer and rain gauge programs amd how they work.
- Create one single program to log data from the anemometer and the rain gauge.
- Use comments to annotate your final code, and explain it's function.

## Reviewing your existing code

Look back at the code you wrote for the anemometer and the rain gauge and review how they worked, what did each line do? To open your code you should type

```bash
nano wind_final.py
```
or
```bash
nano rain_interrupt.py
```

## Creating a single solution

Having 2 programs, one for each sensor, can be helpful but ideally we would want to run one program that monitored all our sensors. Your task this lesson is to combine you code together to create one program to perform both jobs.

To get you started here a few things to think about:
1. Are you going to start a new program and write the program from scratch using the original 2 as guides?

  ```bash
  nano wind_rain.py
  ```

2. Or are you going to copy one of the originals and add to that?
  ```bash
  cp wind_final.py wind_rain.py
  nano wind_rain.py
  ```

3. Are there any lines of code that appear in both prgrams that only need to appear once? For example:

```python
import RPi.GPIO as GPIO,time
```

Is only needed once at the beginning of our program.

4. What variable names are you going to use, in each program so far you have used the variable `count` which won't work if you are counting rain and wind signals.

5. Both programs contain a loop of some kind to display the current readings, these will need to be combined.

## Code Commenting
We haven't used comments much in our work so far but should be really. Comments allow you to annotate and explain what your code is doing. This is useful both for yourself and others reading to code. Adding a comment is quite straight forward. In the example below the line beginning with a `#` has been used, this is ignored by the computer but readable by humans.

```python
#The spin function is called whenever a spin is detect, it increments the count variable and print it out

def spin(channel):
global count
count = count + 1
...
```

## Test & Review
Once you have completed you code you should test it carefully to it functions correctly, reliably and accurately.

If you are happy with your code and how it functions speed some time comparing your code with others and consider the following:
- Is you code exactly the same or are their multiple solutions?
- How clear is their code have they used comments to explain it?
- What improvements coud they make to improve their code?
- What ideas might you take from their code to improve yours?


## What's Next?
- Congratulations you are now able to deploy a basic version of the weather station which displys data on rainfall and wind speed.
- Consider what's missing from this solution, clearly only 2 of the sensors have been covered but what else?
    - Is this the best way to display the data?
    - Is data being saved, could I look back at previous data?

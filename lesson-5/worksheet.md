# Lesson 5 - Combining our code

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

They probably look someting like this:

|Rain Gauge|Anemometer|
|----------|----------|
|```python
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

pin = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
  ``` | ```python
  #!/usr/bin/python
  import RPi.GPIO as GPIO
  import time

  pin = 27

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
    ``` |


## Creating a single solution

Having 2 programs, one for each sensor, can be helpful but ideally we would want to run one program that monitored all our sensors. Your task today i

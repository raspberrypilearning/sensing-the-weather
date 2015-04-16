Firstly, show the class the rain gauge and ask pupils how the device might work and generate a meaningful rain measurement. Then remove the bucket by gently squeezing the clips on either side; the lid should then pop off.

![](images/rain_guage_open.jpg)

This rain gauge is basically a self-emptying tipping bucket. Rain is collected and channelled into the bucket. Once enough rainwater has been collected the bucket will tip over, the water will drain out from the base, and the opposite bucket will come up into position.

What information do we need in order to calculate a rainfall measurement?

- How much water will tip the bucket?
- How many bucket tips have happened?

If we know both of those the answer is easy: *Bucket volume multiplied by number of tips.*

The product [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf) tells us that 0.2794 mm of rain will tip the bucket, so we just need to know how many bucket tips have happened. To get that information, we need to program the Raspberry Pi to detect when the bucket tips and keep a count.

If you look at the RJ11 plug on the end of the wire attached to the rain gauge, you'll see there are only two wires inside: one red and one green. Think of these as the two jumper wires from last time. Now take a close look at the ridge between the two buckets. Inside this is a small cylindrical magnet that points towards the back wall. Inside the back wall there is a clever piece of electronics called a *reed switch*, pictured below.

![](images/reed_switch.jpg)

The reed switch has two metal contacts inside it which will touch together when under the influence of a magnet. Therefore, electronically, this works in exactly the same way as the two jumper wires from the previous lesson. When the bucket tips, the magnet passes the reed switch, causing it to close momentarily. So we can use a *pull up* or *pull down* circuit to detect this, just like before.

The top of the back wall does come off if you want to see inside; just pull on the flat end gently and it should release. Inside there is a small circuit board that you can remove to examine. In the middle of it you will see the reed switch. Replace the circuit board and back wall lid before continuing. Leave the outer funnel/lid off for now.

### Check the code from last lesson

1. Students will first need to check their `pullup.py` code from last lesson and adapt it to use the correct pin for the rain gauge (pin 6).
2. They should then connect some jumper wires and test that their code works as expected.

### Counting bucket tips

1. Currently, our code can tell us whether the GPIO signal is `HIGH` or `LOW`. We need to count the tipping of the bucket, when the signal goes from `HIGH` to `LOW`.
2. Students need to add some variables to their code in order to track the tipping.

|Variable|Purpose|
|--------|-------|
|Count| Used to keep a count of the number of bucket tips.|
|Current_state|Each time the input pin is checked, the state `HIGH` or `LOW` is stored here.|
|Previous_state|Each time the input pin is checked, the current_state is moved to previous_state. We can then compare the two to see if they have changed.|

3. Once their code counts the number of tips, they can multiply this by **0.2794** to get the amount of rainfall. Their code should end up looking something like this:

    ```python
    #!/usr/bin/python
    import RPi.GPIO as GPIO
    import time

    pin = 6

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)

    count = 0
    current_state = 0
    previous_state = 0

    while True:
        current_state = GPIO.input(pin)

        if previous_state == GPIO.HIGH and current_state == GPIO.LOW:
            count=count + 1
            print (count * 0.2794)

        previous_state = current_state
        time.sleep(0.01)
    ```

### Using interrupt handling  

Currently, our code uses a technique called polling to check the status of the pin over and over again. This is inefficient as it is checking the pin all the time, even if there is no rain.

A more sensible and efficient technique is to use interrupts to only pay attention to the pin when it is triggered. This allows the program to do other things whilst still tracking the pin status.

1. There are two key bits of code that we need to add to make this work. First we create a function to count the bucket tips:

  ```python
  def bucket_tipped(channel):
      global count
      count = count + 1
      print (count * 0.2794)
  ```

This function retrieves the current global value of `count`, increments it and displays the current measurement.

2. We then need to set up an interrupt to call this function every time the signal falls from `HIGH` to `LOW`:

  ```
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
  GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped,bouncetime=300)
  ```

The `bouncetime` setting is the minimum amount of time between detections, which can be customised.

3. Their final code should look something like this:

  ```python
  #!/usr/bin/python
  import RPi.GPIO as GPIO

  pin = 6
  count = 0

  def bucket_tipped(channel):
      global count
      count = count + 1
      print (count * 0.2794)

  GPIO.setmode(GPIO.BCM)
  GPIO.setup(pin, GPIO.IN, GPIO.PUD_UP)
  GPIO.add_event_detect(pin, GPIO.FALLING, callback=bucket_tipped, bouncetime=300)

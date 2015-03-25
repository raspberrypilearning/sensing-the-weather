# Lesson 1 - Example

...

## First step

...






Calibration is the practise of adjusting the value reported by a sensor to match a scientifically known value. In order to do this for the anemometer you would need a wind tunnel in your school where you could control the wind speed to an exact value. Since most of us don't have this available we'll need to make do.

Generally speaking anemometers tend to report the wind speed slightly lower than it actually is, a problem which gets progressively worse as the wind speed increases. We can check the [datasheet](https://www.argentdata.com/files/80422_datasheet.pdf) which says

 *A wind speed of 1.492 MPH (2.4 km/h) causes the switch to close once per second*. (although it means 1 revolution or 2 signals)

This means that over our 5 second interval if we have 5 revolutions (10 signals) this should equate to 2.4 km/h.

1. Run the code and remember to use the `sudo` command:

  `sudo ./wind_speed.py`

	You don't need to worry about getting the interrupts to occur at exactly one second intervals here, get a pupil to  spin the anemometer and stop it when the number reaches 10.

  ```
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  2.03575203953 kph
  ```

  This doesn't match the 2.4 kph quoted in the datasheet, this is some of the wind's energy is lost through friction in the sensor, to compensate for this we need to multiply by a factor of 1.18.

1. Press `Ctrl - C` to exit your program.

  Let's test it. First we need to change our code, enter the command below:

    `nano wind_speed.py`

    Find the `calculate_speed` function and modify the last line so that it reads `return km_per_hour * 1.18`.
   
   ```python
    def calculate_speed(r_cm, time_sec):
        global count
        circ_cm = (2 * math.pi) * r_cm
        rot = count / 2.0
        dist_km = (circ_cm * rot) / 100000.0 # convert to kilometres
        km_per_sec = dist_km / time_sec
        km_per_hour = km_per_sec * 3600 # convert to distance per hour
        return km_per_hour * 1.18
    ```

1. Press `Ctrl - O` then `Enter` to save, followed by `Ctrl - X` to quit from nano.

1. Run the code and remember to use the `sudo` command:

  `sudo ./wind_speed.py`

1. Repeat the experiment again and stop spinning the anemometer when the number reaches 10, so again 5 complete rotations over 5 seconds.

  ```
  1
  2
  3
  4
  5
  6
  7
  8
  9
  10
  2.40218740664 kph
  ```

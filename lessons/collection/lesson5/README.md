[Previous lesson](../lesson4/README.md)

# Lesson 5: The wind vane

![](../../../images/wind_vane.png)

## Introduction

## Resources

Students should work in pairs. Each pair will require the following equipment:

- Raspberry Pi
- Weather Station Expansion Board
- Wind vane
- Micro USB power adaptor
- An SD Card with Raspbian already set up through NOOBS
- USB keyboard
- USB mouse
- HDMI cable
- A monitor or TV
- A small phillips screwdriver

## Learning Objectives

- Understand how the wind vane works
- Be able to differentiate between analogue and digital signals
- Understand the purpose of an Analogue to Digital Converter
- Understand digital communication using the I²C protocol
- Use these technologies to determine the direction the wind vane is pointing

## Starter

A wind vane shows the direction *from which* the wind is coming, not where it's going (this can be confusing because TV weather maps show it the other way around). It works by the wind exerting force on a vertical blade which rotates to finds the position of least resistance, this position is then aligned with the direction of the oncoming wind.

Also known as a weather vane these are often found as decorative adornments at the highest point on buildings or churches. Typically taking the shape of a cockerel, horse or ship.

The wind vane is the most complex of the sensors studied so far. It does use reed switches and magnets but it works in a completely different way. Ask the students to pull the top off their wind vane, it should come off without much force. On the underside you'll again find the metal cylinder which is the magnet.

![](../../../images/wind_vane_magnet.png)

*Note: Disassembling the next part is only recommended for students with good motor skills. Younger students may have difficulty reassembling it.*

Next take the screwdriver and remove the three screws in the base, slide the base panel down the cable a bit to get it out of the way. If you look inside now you'll see there are eight reed switches arranged like the spokes of a wheel. Remove the three remaining screws allowing the circuit board to come free. Do not lose these screws.

![](../../../images/wind_vane_reed.png)

Examine the green side of the circuit board now.

## Main Development

### Setting up your Pi

1. Place the SD card into the slot of your Raspberry Pi.
1. Connect the Weather Expansion Board to the GPIO pins.
1. Connect the wind vane to the socket marked *WIND* on the Weather Expansion Board.
1. Next connect the HDMI cable from the monitor or TV.
1. Plug in the USB keyboard and mouse.
1. Plug in the micro USB power supply.
1. When prompted to login type:

    ```bash
    Login: pi
    Password: raspberry
    ```

## Plenary

[Next lesson](../lesson6/README.md)

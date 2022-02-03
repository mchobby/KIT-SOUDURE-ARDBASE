""" i10_tone.py - ARDBASE mini lab - play a tone on the piezo.

	Code is the same for Pico and PYBStick-RP2040

* Author(s): Meurisse D., MCHobby (shop.mchobby.be).

Products:
---> Kit Soudure ARDBASE : https://shop.mchobby.be/product.php?id_product=1124
---> Raspberry-Pi PICO   : https://shop.mchobby.be/product.php?id_product=2025
---> PYBStick-RP2040     : https://shop.mchobby.be/product.php?id_product=2331
------------------------------------------------------------------------

History:
  03 february 2022 - Dominique - initial MicroPython writing
"""

from machine import Pin, PWM
import time

buzz_pin = Pin( 13, Pin.OUT, value=False )
buzz = PWM( buzz_pin )

# Play a Do (at 261 Hertz)
buzz.freq( 261 )
# Max Value=65535, 50% Duty cycle = 65535/2 = 32767
buzz.duty_u16( 32767 )

# Playing the note for 1 second
time.sleep_ms( 1000 )

# Stop the note
buzz.duty_u16( 0 )

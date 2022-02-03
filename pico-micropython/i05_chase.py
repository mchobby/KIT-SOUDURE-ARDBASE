""" i05_chase.py - ARDBASE mini lab - chase between the RED/Orange/Green LEDs

	Code is the same for Pico and PYBStick-RP2040

* Author(s): Meurisse D., MCHobby (shop.mchobby.be).

Products:
---> Kit Soudure ARDBASE : https://shop.mchobby.be/product.php?id_product=1124
---> Raspberry-Pi PICO   : https://shop.mchobby.be/product.php?id_product=2025
---> PYBStick-RP2040     : https://shop.mchobby.be/product.php?id_product=2331
------------------------------------------------------------------------

History:
  02 february 2022 - Dominique - initial MicroPython writing
"""

from machine import Pin
import time

# 6 = LED Rouge/Red
# 7 = LED Orange
# 8 = LED Green
red = Pin( 6, Pin.OUT )
ora = Pin( 7, Pin.OUT )
gre = Pin( 8, Pin.OUT )
sequence = [ red, ora, gre, ora ]

while True:
	for led in sequence:
		led.value( True )
		time.sleep_ms( 100 )
		led.value( False )

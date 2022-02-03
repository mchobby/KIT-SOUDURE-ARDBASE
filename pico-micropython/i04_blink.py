""" i04_blink.py - ARDBASE mini lab - Blink the RED LED

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

while True:
	red.value(1) # value(True)
	time.sleep( 1 )
	red.value(0) # value(False)
	time.sleep( 1 )

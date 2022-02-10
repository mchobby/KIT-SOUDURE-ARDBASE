""" i04_blink.py - ARDBASE mini lab - Blink the RED LED

	Code is for MicroPython Pyboard

* Author(s): Meurisse D., MCHobby (shop.mchobby.be).

Products:
---> Kit Soudure ARDBASE : https://shop.mchobby.be/product.php?id_product=1124
---> MicroPython Pyboard : https://shop.mchobby.be/product.php?id_product=570
------------------------------------------------------------------------

History:
  08 february 2022 - Dominique - initial MicroPython writing
"""

from machine import Pin
import time

# X4 = LED Rouge/Red
# X3 = LED Orange
# X2 = LED Green
red = Pin( "X4", Pin.OUT )

while True:
	red.value(1) # value(True)
	time.sleep( 1 )
	red.value(0) # value(False)
	time.sleep( 1 )

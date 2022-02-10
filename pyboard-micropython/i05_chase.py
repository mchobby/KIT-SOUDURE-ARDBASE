""" i05_chase.py - ARDBASE mini lab - chase between the RED/Orange/Green LEDs

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
ora = Pin( "X3", Pin.OUT )
gre = Pin( "X2", Pin.OUT )
sequence = [ red, ora, gre, ora ]

while True:
	for led in sequence:
		led.value( True )
		time.sleep_ms( 100 )
		led.value( False )

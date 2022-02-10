""" i07_pot.py - ARDBASE mini lab - read the potentiometer value and convert
                 it to voltage (between 0 & 3.3V).

	Code for MicroPython Pyboard

* Author(s): Meurisse D., MCHobby (shop.mchobby.be).

Products:
---> Kit Soudure ARDBASE : https://shop.mchobby.be/product.php?id_product=1124
---> MicroPython Pyboard : https://shop.mchobby.be/product.php?id_product=570
------------------------------------------------------------------------

History:
  08 february 2022 - Dominique - initial MicroPython writing
"""

from machine import Pin, ADC
import time

adc = ADC( "X20" ) 

while True:
	# Return a value between 0 & 65535
	val = adc.read_u16()
	volts = 3.3 * val / 65535
	print( 'Val: %5i  Volts: %5.3f' % (val,volts) )
	time.sleep_ms( 100 )

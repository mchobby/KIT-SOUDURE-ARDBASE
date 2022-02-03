""" i08_ldr.py - ARDBASE mini lab - read the photoresistor value and calculate
        the max value and min value for the LDR response.

	May produce a result like the following:
	Val: 59550,  min: 13059, max: 59678 (min= covered, max= exposed to light)

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

from machine import Pin, ADC
import time

adc = ADC( 1 ) # ADC(1) on GPIO27

# Used to find the min and max value
_max = 0
_min = 65535
while True:
	# Return a value between 0 & 65535
	val = adc.read_u16()
	# Identify the minimum & maximum value for the LDR
	_min = min( val, _min )
	_max = max( val, _max )
	print( 'Val: %5i,  min: %5i, max: %5i' % (val,_min,_max) )
	time.sleep_ms( 100 )

""" i09_ldr.py - ARDBASE mini lab - read the TMP36 analog sensor temperature

	Code is for MicroPython Pyboard

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

adc = ADC( "X22" ) # ADC(0) on GPIO26

while True:
	# Return a value between 0 & 65535
	val = adc.read_u16()
	volts = 3.3 * val / 65535
	# convert voltage to temperature
	temp = (volts-0.5)*100
	print( 'Val: %5i,  Volts: %5.3f, Temp: %5.3f' % (val,volts,temp) )
	time.sleep_ms( 100 )

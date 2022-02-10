""" i01_button.py - ARDBASE mini lab - Test button

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

btn = Pin( "X12", Pin.IN )
while True:
	value = btn.value()
	# Attention --> Logique inversée
	# value = 0 : Bouton pressé
	# value = 1 : Bouton relâché
	print( 'Value: ', value, 'Pressed' if value==0 else 'Release' )
	time.sleep_ms( 100 )

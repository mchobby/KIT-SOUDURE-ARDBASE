""" i01_button.py - ARDBASE mini lab - Test button 

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

btn = Pin( 2, Pin.IN )
while True:
	value = btn.value()
	# Attention --> Logique inversée
	# value = 0 : Bouton pressé
	# value = 1 : Bouton relâché
	print( 'Value: ', value, 'Pressed' if value==0 else 'Release' )
	time.sleep_ms( 100 )

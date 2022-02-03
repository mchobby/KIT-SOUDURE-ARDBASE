""" i02_button.py - ARDBASE mini lab - Test button
    Using the Signal class to get the button state with positive logic

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

from machine import Pin, Signal
import time

btn = Pin( 2, Pin.IN )
sig = Signal( btn, invert=True )
while True:
	value = sig.value()
	# Logique POSITIVE !!!
	# value = 1 : Bouton pressé
	# value = 0 : Bouton relâché
	print( 'Value: ', value, 'Pressed' if value==1 else 'Release' )
	time.sleep_ms( 100 )

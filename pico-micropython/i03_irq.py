""" i03_irq.py - ARDBASE mini lab - Using button with IRQ

    (This is an advanced example)

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
import micropython
micropython.alloc_emergency_exception_buf(100)

def btn_pressed( pin ):
	print( "Hey... Button pressed")

btn = Pin( 2, Pin.IN )
# Signal is Falling to Ground when the button is pressed
# The handler function is called when IRQ is triggered
btn.irq( trigger=Pin.IRQ_FALLING, handler=btn_pressed )

# Now press the button & see the magic of Interrupt Request (IRQ)

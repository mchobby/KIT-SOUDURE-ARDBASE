""" i03_irq.py - ARDBASE mini lab - Using button with IRQ

    (This is an advanced example)

	Code is for the MicroPython Pyboard

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
import micropython
micropython.alloc_emergency_exception_buf(100)

def btn_pressed( pin ):
	print( "Hey... Button pressed")

btn = Pin( "X12", Pin.IN )
# Signal is Falling to Ground when the button is pressed
# The handler function is called when IRQ is triggered
btn.irq( trigger=Pin.IRQ_FALLING, handler=btn_pressed )

# Now press the button & see the magic of Interrupt Request (IRQ)

""" i10_tone.py - ARDBASE mini lab - play a tone on the piezo.
	based on https://wiki.mchobby.be/index.php?title=MicroPython-Hack-piezo
	Code is for MicroPython Pyboard

* Author(s): Meurisse D., MCHobby (shop.mchobby.be).

Products:
---> Kit Soudure ARDBASE : https://shop.mchobby.be/product.php?id_product=1124
---> MicroPython Pyboard : https://shop.mchobby.be/product.php?id_product=570
------------------------------------------------------------------------

History:
  08 february 2022 - Dominique - initial MicroPython writing
"""

from pyb import Pin, Timer
import time

# Configurer les broches PWM pour la sortie sur buzzer
pin_buzz = Pin("X1") # Broche X1 avec timer 1 et Channel 1
tim = Timer(2, freq=3000)
ch = tim.channel(1, Timer.PWM, pin=pin_buzz)

def play_freq( freq ):
	global tim, ch
	if freq == 0:
		ch.pulse_width_percent( 0 )
	else:
		tim.freq( freq )
		ch.pulse_width_percent( 30 )

# Play a Do (at 261 Hertz)
play_freq( 261 )
# Playing the note for 1 second
time.sleep_ms( 1000 )
# Stop the note
play_freq( 0 )

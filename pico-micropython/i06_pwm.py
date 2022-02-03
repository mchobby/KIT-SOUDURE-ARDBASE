""" i06_pwm.py - ARDBASE mini lab - control the red LED power with PWM

	Code is the same for Pico and PYBStick-RP2040

* Author(s): Meurisse D., MCHobby (shop.mchobby.be).

Products:
---> Kit Soudure ARDBASE : https://shop.mchobby.be/product.php?id_product=1124
---> Raspberry-Pi PICO   : https://shop.mchobby.be/product.php?id_product=2025
---> PYBStick-RP2040     : https://shop.mchobby.be/product.php?id_product=2331
------------------------------------------------------------------------

History:
  07 february 2022 - Dominique - initial MicroPython writing
"""

from machine import Pin, PWM
import time

# 6 = LED Rouge/Red
# 7 = LED Orange
# 8 = LED Green
red_pin = Pin( 6, Pin.OUT )
red_pwm = PWM( red_pin )
# red_pwm.freq( 200 ) # default PWM freq = 500 Hz

while True:
	# ligthing up
	for ratio in range( 0, 65001, 1000 ): # 0 to 65000 by step of 1000
		red_pwm.duty_u16( ratio )
		time.sleep_ms( 10 )
	# ligthing down
	for ratio in range( 0, 65001, 1000 ):
		red_pwm.duty_u16( 65534-ratio )
		time.sleep_ms( 10 )

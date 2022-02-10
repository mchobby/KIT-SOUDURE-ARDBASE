""" i06_pwm.py - ARDBASE mini lab - control the red LED power with PWM

	REQUIRES pwm.py library
	https://github.com/mchobby/pyboard-driver/blob/master/UNO-R3/lib/pwm.py

	Code is for the MicroPython Pyboard

* Author(s): Meurisse D., MCHobby (shop.mchobby.be).

Products:
---> Kit Soudure ARDBASE : https://shop.mchobby.be/product.php?id_product=1124
---> MicroPython Pyboard : https://shop.mchobby.be/product.php?id_product=570
------------------------------------------------------------------------

History:
  8 february 2022 - Dominique - initial MicroPython writing
"""

import time
# https://github.com/mchobby/pyboard-driver/blob/master/UNO-R3/lib/pwm.py
from pwm import *

# X4 = LED Rouge/Red
# X3 = LED Orange
# X2 = LED Green
red_pwm = pwm( "X4" ) # PWM freq = 500 Hz
while True:
	# ligthing up
	for ratio in range( 0, 100 ): # 0 to 100%
		red_pwm.percent = ratio
		time.sleep_ms( 10 )
	# ligthing down
	for ratio in range( 0, 100 ):
		red_pwm.percent = 100-ratio
		time.sleep_ms( 10 )

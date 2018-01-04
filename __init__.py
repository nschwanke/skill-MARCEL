# Copyright 2018 Noah Schwanke
# This file is part of the MARCEL skill for the Clam Box Virtual Assistant
from os.path import dirname

import mycroft.util
import time
import requests
import json
import threading
import sys
from os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import GPIO

from adapt.intent import IntentBuilder

from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'nschwanke'

LOGGER = getLogger(__name__)

class MarcelSkill(MycroftSkill):
		def __init__(self):
				super(MarcelSkill, self).__init__(name="MarcelSkill")

		def initialize(self):
				directions_bathroom_intent = IntentBuilder("DirectionsBathroomIntent"). \
						require("DirectionsBathroomKeyword").build()
				self.register_intent(directions_bathroom_intent, self.handle_directions_bathroom_intent)

				# -------------------------------------------------------------------------------
				hours_intent = IntentBuilder("HoursIntent"). \
						require("HoursKeyword").build()
				self.register_intent(hours_intent, self.handle_hours_intent)

				# -------------------------------------------------------------------------------
        
		def handle_directions_bathroom_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("directions.bathroom")
				time.sleep(1) 				
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","Off")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO4","On")
				
		def handle_hours_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("hours")
				time.sleep(1) 				
				GPIO.set("GPIO2","On")
				GPIO.set("GPIO3","Off")

				try:
					start = time.time()
					mycroft.util.wait_while_speaking()
					end = time.time()
					if (end - start) < 1:
						time.sleep(10)
				except:
					time.sleep(10)

				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO4","On")


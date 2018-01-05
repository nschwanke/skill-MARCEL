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
				condiments_intent = IntentBuilder("CondimentsIntent"). \
						require("CondimentsKeyword").build()
				self.register_intent(condiments_intent, self.handle_condiments_intent)

				# -------------------------------------------------------------------------------
				menu_seafoodplate_intent = IntentBuilder("MenuSeafoodplateIntent"). \
						require("MenuSeafoodplateKeyword").build()
				self.register_intent(menu_seafoodplate_intent, self.handle_menu_seafoodplate_intent)

				# -------------------------------------------------------------------------------
				funfact_intent = IntentBuilder("FunfactIntent"). \
						require("FunfactKeyword").build()
				self.register_intent(funfact_intent, self.handle_funfact_intent)

				# -------------------------------------------------------------------------------
				alcohol_intent = IntentBuilder("AlcoholIntent"). \
						require("AlcoholKeyword").build()
				self.register_intent(alcohol_intent, self.handle_alcohol_intent)

				# -------------------------------------------------------------------------------
				recommended_intent = IntentBuilder("RecommendedIntent"). \
						require("RecommendedKeyword").build()
				self.register_intent(recommended_intent, self.handle_recommended_intent)

				# -------------------------------------------------------------------------------
				icecream_intent = IntentBuilder("IcecreamIntent"). \
						require("IcecreamKeyword").build()
				self.register_intent(icecream_intent, self.handle_icecream_intent)

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

		def handle_condiments_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("condiments")
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
				
		def handle_menu_seafoodplate_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("menu.seafoodplate")
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
				
		def handle_funfact_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("funfact")
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
				
		def handle_alcohol_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("alcohol")
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
				
		def handle_recommended_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("recommended")
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
				
		def handle_icecream_intent(self, message):
				GPIO.set("GPIO2","Off")
				GPIO.set("GPIO3","On")
				GPIO.set("GPIO4","Off")
				time.sleep(1)
				self.speak_dialog("icecream")
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



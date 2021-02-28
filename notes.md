Release one, notes: The app is built with an oop based system, all prefix data is given by a call,
the main reason of this is to be able to write a function later which can get device saved data
and implement it to the app logic, as currently my file-writing system isnt working 
(although MB states that it has 30kb of storage, excluding the hex file storage, as the complete storage is 256kb)
================================================================

"""
software info: 
screens: {
	1=home
	2=screen count
	3=paint
	4=snake


}
"""
from microbit import *
from time import sleep as tsleep


class app:
	def __init__(self, _usn, _age, _sc, _Apps):
		''' user data related '''
		self.cuUsername = _usn
		self.cuAge = _age
		''' system state related '''
		self.screenCount = _sc
		self.apps = _Apps
		self.curScreen = 1
		# will be able to view if it is none or "some" during if/else
		self.app = None
		self.curScreenIndex = 0


	def startOs(self):
		# animating the startup
		self.startUpAnimation()
		# starting the app loop
		while True:
			display.show(self.curScreen)
			# checking if they want to enter the app
			if button_a.is_pressed() and button_b.is_pressed():
				self.openApp(self.apps[self.curScreen-1])
				
			# button a and b change current screens, with left-right logic
			if button_a.is_pressed():
				self.changeScreen("L")
			if button_b.is_pressed():
				self.changeScreen("R")




	def openApp(self, _ato):
		# checking which app they meant to open
		if _ato == "Home":
			self.Home()


	def changeScreen(self, _dir):
		if _dir == "L":
			if self.curScreen > 1:
				tsleep(0.3)
				self.curScreen -= 1
		if _dir == "R":
			if self.curScreen < self.screenCount:
				tsleep(0.3)
				self.curScreen += 1

	def startUpAnimation(self):
		# creating a startup animation
		vgn = 0
		for i in range(5):
			tsleep(0.2)
			for i in range(5):
				display.set_pixel(vgn, i, 9)
			vgn+=1
		#display.scroll("SMB 1")
		#display.scroll("Hello " + self.cuUsername)


	def Home(self):
		homeGrid = [
					[0,0,0,0,0],
					[0,0,0,0,0],
					[0,0,0,0,0],
					[0,0,0,0,0],
					[0,0,0,0,0]
				]
		display.show("YO")
		curCursLoc = [4,4]

		# setting the apps in screens
		for x in range(len(homegrid[0])):
			for y in range(len(homegrid)):
				

	




		# filling the homegrid
		while not(accelerometer.was_gesture("shake")):
			set_pixel(cur)









# Home, settings, paint, radio will always exist in screens
runApp = app("Adak",14, 5, ["Home", "Settings", "Paint", "Radio", "EatFruits"])
runApp.startOs()

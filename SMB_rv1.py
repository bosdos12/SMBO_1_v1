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
					[1,0,1,0,1],
					[0,0,0,0,0],
					[1,0,1,0,1],
					[0,0,0,0,0],
					[0,0,0,0,0]
				]
		display.clear()
		curCursLoc = [4,4]

		# setting the homegrid array and the screen via a basic algorithm
		atc=0
		for x in range(len(homeGrid)):
			print(atc)
			if x % 2 == 0:
				for y in range(len(homeGrid)):
					if y % 2 == 0:
						if atc < len(self.apps):
							homeGrid[x][y] = self.apps[atc]
							display.set_pixel(x, y, 5)
							atc+=1
						else:
							homeGrid[x][y] = 0
						
			else:
				for y2 in range(len(homeGrid)):
					if y2 % 2 != 0:
						if atc < len(self.apps):
							homeGrid[x][y2] = self.apps[atc]
							display.set_pixel(x, y2, 5)
							atc+=1
						else:
							homeGrid[x][y2] = 0

		# starting the actual app full proccess
		while not(accelerometer.was_gesture("shake")):
			# rendering the current user
			display.set_pixel(curCursLoc[0], curCursLoc[1], 9)
			''' checking for input '''

			def changeCursorLoc(orientation):
				# setting the orientation number basedd of the type of movement the user wants
				# as our movements are 2d, 0 will move the cursor horizontally, 1 will move it vertically via array changes
				# this approach also cuts back a lot of lines of unneeded code
				orientationNum = 0
				if orientation == "y":
					orientationNum = 1
					
				# checking if the grid location contains a pointer to an application
				if homeGrid[curCursLoc[0]][curCursLoc[1]] != 0:
					display.set_pixel(curCursLoc[0],curCursLoc[1], 5)
				else:
					display.set_pixel(curCursLoc[0],curCursLoc[1], 0)

				# doing some orientation specific calculations
				if orientation == "x":
					if curCursLoc[orientationNum] < 4:
						curCursLoc[orientationNum]+=1
					else:
						curCursLoc[orientationNum]=0
				else:
					if curCursLoc[orientationNum] > 0:
						curCursLoc[orientationNum]-=1
					else:
						curCursLoc[orientationNum]=4

				
			# if button a is pressed, moving the cursor horizontally
			if button_a.is_pressed():
				tsleep(0.3)
				changeCursorLoc("x")
			# if button b is pressed, moving the cursor vertically
			if button_b.is_pressed():
				tsleep(0.3)
				changeCursorLoc("y")
				

	


# Home, settings, paint, radio will always exist in screens
runApp = app("Adak",14, 5, ["Home", "Settings", "Paint", "Radio", "EatFruits"])
runApp.startOs()
 

class Battery(object):
	def __init__(self, battery):
		self.battery = battery
	def changeBattery(self):
		self.battery = self.battery - 1 #lowers battery by 1
		return self.battery
#the battery class is not a scene because the user doesn't enter it - it just contains a method to change the battery which is accessed by the engine class

import Battery

class Engine(object): #runs the game
	def __init__(self, scene_map):
		self.scene_map = scene_map #the engine will use the scene map that came from the map class
	def play(self, start_battery):
		#everytime you play the game it will print the little context summary
		print("Your grandfather's funeral was a week ago. You were very close to him, but nearing his death, it seemed like he was hiding something from you. For some reason, he left you this computer in his will. You power up the computer and it seems that the only way to navigate through the files is with a very basic command line interface.")
		print("Use 'cd' to change directories, 'ls' to to list the files in the working directory, 'pwd' to print the working directory, and 'open' to open files.")
		print("But watch out! The battery drains quickly on this computer and you don't have any way of charging it!")
		self.battery = start_battery #the start_battery comes from the game file
		current_scene = self.scene_map.opening_scene() #before the while loop is run, the current_scene will be the first scene
		current_battery = self.battery #current battery is self.battery
		previous_scene = 0 #honestly looking at this im a little confused - is it referring to the number in the scenes list in map
		last_scene = self.scene_map.next_scene('finish')
		print("battery: " + str(self.battery) + "%") #how to print battery level
		while current_scene != last_scene and self.battery != 0: #loops through scenes while user is not finished AND the battery has not run out
			previous_scene = current_scene #the current_scene becomes the previous_scene
			next_scene_name = current_scene.enter() #the next scene name is returned by the current_scene class in the enter method
			current_scene = self.scene_map.next_scene(next_scene_name) #the next_scene becomes the current_scene - we get that by going into the map class and inputting the scene name into the list of scenes to get the actual class and make a new instance of it
			self.battery = Battery.Battery(self.battery).changeBattery() #every time the user starts a new scene, the battery goes down 1%
			print("battery: " + str(self.battery) + "%") #the battery level is printed every time a new scene is entered
		if self.battery == 0: #if you run out of battery you lose
 			current_scene = Death() #death isn't really death, but it happens when you lose - maybe the computer electrocutes you idk 
		current_scene.enter() #goes to the next scene
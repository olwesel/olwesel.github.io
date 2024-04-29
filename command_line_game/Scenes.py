class Scene(object): #if there were something specific to scenes that aren't directories it would go in here
	def __init__(self):
		pass
	def enter(self):
		pass

class Directory(Scene): #class for any folder
	def __init__(self):
		self.ld = self.wd.split("/")
		self.ld = self.ld[len(self.ld)-1]
		self.all_paths = [ #all directories in this game
			'users/grandpa',
			'users/grandpa/desktop',
			'users/grandpa/documents',
			'users/grandpa/music',
			'users/grandpa/photos',
			'users/grandpa/documents/recipes',
			'users/grandpa/documents/poetry',
			'users/grandpa/documents/contacts',
			'users/grandpa/documents/notes',
			'users/grandpa/gold'
		]
	def enter(self): #commands that every directory can accept
		self.action = input("mycomputer:"+self.ld+" grandpa$ ")
		self.val = self.wd
		if " " not in self.action:
			if self.action == "cd":
				self.val = 'users/grandpa'
			if self.action == "pwd":
				print(self.wd)
				self.val = self.wd
			if self.action == "ls":
				for line in self.contents:
					print(line)
				self.val = self.wd
		else:
			self.command_find = self.action.split(" ")
			if self.command_find[0] == 'cd':
				self.input_path = self.command_find[1]
				for path in self.all_paths:
					if self.wd in path:
						new_path = path[len(self.wd)+1:len(path)]
						#print(new_path)
						if self.input_path == new_path:
							self.val = path
		return self.val

#below are all the scenes (including directories)
class UserFolder(Directory):
	def __init__(self):
		self.wd = 'users/grandpa'
		self.ld = 'grandpa'
		self.contents = ['desktop', 'documents', 'music', 'photos']
		super(UserFolder, self).__init__()
	def enter(self):
		super(UserFolder, self).enter()
		return self.val

class Desktop(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/desktop'
		self.ld = 'desktop'
		self.contents = ['Read me!.txt']
		super(Desktop, self).__init__()
	def enter(self):
		super(Desktop, self).enter()
		if self.action == 'open Read me!.txt':
			print("To my favorite grandchild (that's you!),")
			print("If you're reading this, it means I have passed away. I have hidden a large amount of gold at an address hidden in my computer. Using clues only you'll be able to solve, I want you to find the address and use the gold to help make the world a better place. You're the only person I trust with my fortune.")
			print("When you were born in 2000, I knew you were special. You will go on to do great things, and I hope I stay close to your heart.")
			print("I love you.")
			print(", Grandpa")
			print("P.S. I was just listening to the album I got you for Christmas when you were 10. You should give it a listen; it might bring back some memories!")
		return self.val

class Documents(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/documents'
		self.ld = 'documents'
		self.contents = ['recipes', 'contacts', 'poetry', 'notes']
		super(Documents, self).__init__()
	def enter(self):
		super(Documents, self).enter()
		return self.val

class Music(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/music'
		self.ld = 'music'
		self.contents = [
 			'Back In Black - AC/DC.mp3',
 			'Into the Void - Black Sabbath.mp3',
 			'Im rlly cool (not) - Dakota Champagne',
			'Let It Be - The Beatles.mp3',
			'Box of Rain - The Grateful Dead.mp3',
			'Vicious - Lou Reed.mp3',
			'You Can Call Me Al - Paul Simon.mp3',
			'C.R.E.A.M. - Wu-Tang Clan.mp3',
			'Python Droolz - The JS Gang.mp3',
			'Python Rules, Actually - Zed Shaw.mp3',
			'Push It - Salt-N-Pepa ft. GitHub.mp3']
		super(Music, self).__init__()
	def enter(self):
		super(Music, self).enter()
		if 'open' in self.action:
			if self.action[5:len(self.action)] == 'Let It Be - The Beatles.mp3':
				print('The song begins to play. Its your grandfather singing to the tune of "Let It Be". He really put a lot of work into this treasure hunt.')
				print('"Let it be, let it be. Plus eleven is the key."')
				print('"Salad has the answer. Use the key."')
			elif self.action[5:len(self.action)] in self.contents:
				print('What a good song.')
		return self.val

class Photos(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/photos'
		self.ld = 'photos'
		self.contents = [
			'05_02_08.jpg',
			'01_09_08.jpg',
			'02_12_10.jpg',
			'21_10_10.jpg',
			'25_12_10.jpg',
			'28_01_11.jpg',
			'04_12_11.jpg',
			'11_12_11.jpg',
			'15_04_12.jpg',
			'29_06_12.jpg',
			'26_01_13.jpg',
			'09_05_14.jpg',
			'01_10_14.jpg',
			'17_06_15.jpg',
			'13_08_15.jpg',
			'27_06_16.jpg',
			'26_11_16.jpg',
			'14_12_16.jpg',
			'04_02_17.jpg',
			'23_12_17.jpg'
			]
		self.descriptions = [
			"It's a photo of your grandpa holding a fish.",
			"It's a photo of you and your little brother eating ice cream.",
			"It's just a photo of the sky.",
			"It's a photo of a painting.",
			"It's a photo of you and your grandfather on Christmas, 2010 holding up the album 'Let it Be' by The Beatles; he got it for you as a gift!",
			"It's a photo of a sunset.",
			"It's a photo of a boat.",
			"It's a photo of your mother reading a book.",
			"It's a photo of you building a sandcastle.",
			"It's a photo of a frog.",
			"It's a photo of a puppy.",
			"It's a photo of a duck.",
			"It's a photo of a lake.",
			"It's a photo of your grandfather in an armchair.",
			"It's a photo of you and your sister on the beach.",
			"It's a photo of a bird.",
			"It's a photo of a horse.",
			"It's a photo of a bonfire.",
			"It's a photo of a goat.",
			"It's a photo of a flower."
			]
		super(Photos, self).__init__()
	def enter(self):
		super(Photos, self).enter()
		if 'open' in self.action:
			for i in range(len(self.contents)):
				if self.action[5:len(self.action)] == self.contents[i]:
					print("The image loads.")
					print(self.descriptions[i])
		return self.val

class Recipes(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/documents/recipes'
		self.ld = 'recipes'
		self.contents = [
		'The Perfect Pizza.pdf',
		'Delish Brownies.pdf',
		'Mac and Cheese.pdf',
		'Caesar Salad.pdf']
		self.descriptions = [
		"It's... just a pizza recipe.",
		"It's... just a brownie recipe.",
		"It's... just a mac and cheese recipe.",
		"I like Caesar Salad. I wonder what else is named after Caesar. Now I'll write some arbitrary letters that don't mean anything... or do they? iwt ephhldgs xh epcxcxegthh. Maybe it's poetry or something."]
		super(Recipes, self).__init__()
	def enter(self):
		super(Recipes, self).enter()
		if 'tr' in self.action:
			if self.action == "echo iwt ephhldgs xh epcxcxegthh | tr [p-za-o] [a-z]":
				print("the password is paninipress")
			else:
				print("I'm not sure you're using the command correctly. Try again or you can always do it by hand!")
		if 'open' in self.action:
			for i in range(len(self.contents)):
				if self.action[5:len(self.action)] == self.contents[i]:
					print(self.descriptions[i])
					if self.action[5:len(self.action)] != self.contents[3]:
						print("Maybe you can make that later when you're not running out of battery power!")
		return self.val
		
class Contacts(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/documents/contacts'
		self.ld = 'contacts'
		self.contents = [
		'Dakota Champagne.txt',
		'Lance Bass.txt',
		'Linda Haspin.txt',
		'Holly Flax.txt',
		'Mel Peabody.txt',
		'Zed Shaw.txt',
		'Victor Crumb.txt']
		super(Contacts, self).__init__()
	def enter(self):
		super(Contacts, self).enter()
		if 'open' in self.action:
			if self.action[5:len(self.action)] == "Linda Haspin.txt":
				print("Linda Haspin")
				print("Address: 38 Pierrepont st apt 11B")
				print("Email: lindahaspin@gmail.com")
				print("Phone number: 7342")
			elif self.action[5:len(self.action)] in self.contents:
				print("That's just a text file with contact information in it. You can visit them later!")
		return self.val

class Poetry(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/documents/poetry'
		self.ld = 'poetry'
		self.contents = [
		'the bluest sky.txt',
		"poems that seem like arbitrary letters but aren't.txt",
		'sunny day.txt',
		'couch poem.txt']
		super(Poetry, self).__init__()
	def enter(self):
		super(Poetry, self).enter()
		if 'open' in self.action:
			if self.action[5:len(self.action)] == self.contents[1]:
				print("echo (encoded message) | tr [(the letter that 'a' would be encoded to)-za-(the letter that x would be encoded to)] [a-z]")
				print("")
				print("")
				print("for example:")
				print("")
				print('INPUT:')
				print('echo gur dhvpx oebja sbk whzcf bire gur ynml qbt | tr [n-za-m] [a-z]')
				print('OUTPUT:')
				print('the quick brown fox jumps over the lazy dog')
				print("")
			elif self.action[5:len(self.action)] in self.contents:
				print("I'm sure that's a great poem but it's not really helpful right now.")
		return self.val

class NotesLocked(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/documents/notes'
		self.ld = 'notes(locked)'
		self.contents = ['contents are password protected']
		super(NotesLocked, self).__init__()
	def enter(self): #the locked version of the notes folder does not super the enter method from directory because none of those commands can work on a locked folder
		print("Looks like you need a password to open this folder.")
		print("")
		guess = raw_input("PASSWORD: ")
		if guess == "paninipress":
			print("correct password")
			self.val = 'notes'
		else:
			print("incorrect password")
			super(NotesLocked, self).enter()
		return self.val

class Notes(Directory):
	def __init__(self):
		self.wd = 'users/grandpa/documents/notes'
		self.ld = 'notes(unlocked)'
		self.contents = [
		'you did it.txt',
		'the pin.txt']
		super(Notes, self).__init__()
	def enter(self):
		super(Notes, self).enter() #Now commands do work
		if 'open' in self.action:
			if self.action[5:len(self.action)] == self.contents[0]:
				print("Go to 220 South Street. Number 178.")
			if self.action[5:len(self.action)] == self.contents[1]:
				print("When I need the pin, I call Linda.")
		return self.val

class Gold(Scene):
	def enter(self):
		print("")
		print("You go to 220 South Street. It's a storage-unit. 178 must be the number of the locker!")
		print("You go to the locker but it asks for a 4-digit pin number. What is it?")		
		return 'locker' #not a directory so there's no 'val' variable

class Locker(Scene):
	def __init__(self):
		self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
	def enter(self):
		guess = raw_input("PIN: ")
		if guess == "7342":
			print("Correct pin.")
			return 'finish'
		for char in guess:
			if char not in self.numbers:
				print("Not a valid input. Try something else.")
				return 'locker'
		print("Incorrect pin. Let's go back to the computer to search for more clues.")
		print("If you want to come back to the storage-unit, just open the 'you did it.txt' document in notes again.")
		return 'users/grandpa'

class Finish(Scene):
	def enter(self):
		print("Congrats! You found the gold! Your grandpa would be proud.")

class Death(Scene):
	def enter(self):
		print("You ran out of battery! I guess you'll never get that gold.")
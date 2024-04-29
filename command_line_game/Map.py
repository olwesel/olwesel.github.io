import Scenes

class Map(object):		
	scenes = { #all the scenes in this game
		'users/grandpa': Scenes.UserFolder(), #all classes from scenes file have to specify import
		'users/grandpa/desktop': Scenes.Desktop(),
		'users/grandpa/documents': Scenes.Documents(),
		'users/grandpa/music': Scenes.Music(),
		'users/grandpa/photos': Scenes.Photos(),
		'users/grandpa/documents/recipes': Scenes.Recipes(),
		'users/grandpa/documents/contacts': Scenes.Contacts(),
		'users/grandpa/documents/poetry': Scenes.Poetry(),
		'users/grandpa/documents/notes': Scenes.NotesLocked(),
		'notes': Scenes.Notes(), #not directories so aren't named by file path
		'gold': Scenes.Gold(),
		'locker': Scenes.Locker(),
		'finish': Scenes.Finish(),
		'death': Scenes.Death()}
	def __init__(self, start_scene):
		self.start_scene = start_scene
	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
	def opening_scene(self):
		return self.next_scene(self.start_scene)
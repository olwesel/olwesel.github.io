import Map
import Engine

a_map = Map.Map('users/grandpa/desktop') #inputs first scene - the path of the start directory
a_game = Engine.Engine(a_map) #starts a new game by creating a new instance of the engine class
a_game.play(100) #sets battery to 100 - so technically if you wanted to change the difficulty level of the game, you could start with a different battery level
#this is the file the user calls to play the game
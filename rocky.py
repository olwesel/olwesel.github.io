file = open("rocky.txt", "r")
text = file.read()
words = text.split(" ")
lines = text.split("\n")
settings = []
numbers1 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")
numbers2 = ("first", "second", "third", "fourth", "fifth")


def main():
	descriptions = listDescriptions(lines)
	characters = listCharacters(listCapitals(descriptions))
	counter = 0

	for character in characters:
		words = wordsSpoken(character[2])
		counter += 1
		most_used_word = ('', 0)
		char_description = whoIs(character, listDescriptions(lines))
	 	char_speaks_num = whenSpeaks(character[2])
	 	print(str(counter) + str(") ") + str(character[0]))
	 	print("Description: " + str(char_description))
	 	if char_speaks_num == 1:
	 		print("This character speaks " + str(char_speaks_num) + " time.")
	 	else:
	 		print("This character speaks " + str(char_speaks_num) + " times.")
	 	for word in words:
	 		if word[1]>most_used_word[1]:
	 			most_used_word = word
	 	if most_used_word[0] != "" and most_used_word[1]>2:
	 		print("This character uses the word " + '"' + str(most_used_word[0]) + '"' + " most frequently; " + str(most_used_word[1]) + " times.")
	 	print("")

def wordCount(a_word):
	times_used = 0
	w = []
	for line in lines:
		w.append(line.split(" "))
	for x in w:
		for item in x:
			word = item.strip(" ,.'/;:-")
			word = word.strip("\t\t\t\t")
			if a_word == word:
				times_used+=1
	return times_used

def listCharacters(caps):
#	dictionary = ("CLOSE-UP", "SHOT", "ANGLE", "'S")
	capitals = caps
	indented_speakers = []
	characters = []
	names = []
	for line in lines:
		if "\t\t\t\t" in line and "\t\t\t\t" not in lines[lines.index(line)+1] and "\t\t\t\t" not in lines[lines.index(line)-1]:
			indented_line = line.strip("\t\t\t\t")
			indented_line = indented_line.replace("(V.O.)", "")
			indented_line = indented_line.strip(" ")
			if indented_line.isupper() and "CONT" not in indented_line and "MORE" not in indented_line and "FADE" not in indented_line and "DISSOLVE" not in indented_line and "CUT TO" not in indented_line and "THE END" not in indented_line and '"' not in indented_line and "'" not in indented_line:
				if indented_line not in indented_speakers:
					indented_speakers.append(indented_line)
	for speaker in indented_speakers:
		character = speaker
		in_capital = False
		sp = speaker.strip("#1 #2 #3 #4 #5 1 2 3 4 5 first second third fourth fifth") #stripped of number
		for capital in capitals:
			if sp in capital:
				in_capital = True
				if (capital[len(capital)-1] == "S" and speaker[len(speaker)-1] != "S"): #eg. when there are ringside commentators, I want to include all 3 as different characters, not as one character named "ringside commentators"
				  	for num in numbers1:
				  		if speaker[len(speaker)-1] == num: #if speaker ends in a number
				  			character = capital.replace("TWO", "")
				  			character = character.replace("THREE", "")
				  			character = character.replace("FOUR", "")
				  			character = (character.rstrip("S")) + " " + "#" + num
				  	for num in numbers2:
				  		if speaker.startswith(num):
				  			character = capital.replace("TWO", "")
				  			character = character.replace("THREE", "")
				  			character = character.replace("FOUR", "")
				  			character = num + " " + (character.rstrip("S"))
				elif sp != capital: #eg. reporter is not the same character as reporter #1 - accounts for when one scene could have multiples of a type of character designated by numbers and another could have only one of the same type of character
					#but this isn't working anymore! 
					character = capital
				if character not in characters:
					characters.append(character)
					names.append([character, capital, speaker])
		if character not in characters and in_capital == False:
			characters.append(character)
			names.append([character, "null", speaker])
		for name1 in names:
			for name2 in names:
				if name1[2] in name2[1] and len(name2[1])>len(name1[1]):
					names.remove(name2)
	return names #this will be in order of who speaks first, not who is introduced first (and is a list of only speaking characters)
#what happened to ringside commontators 1 and 2??

def listCapitals(desc):
	capitals = []
	joint_capitals = []
	dwords = []
	consecutives = []
	for pair in desc:
	 	dwords.append(pair[1].split(" "))
	for description in dwords:
		for i in range(len(description)):
			word = description[i].strip(".,!")
			if word.isupper() and "'S" not in word:
				capitals.append((word, i))
	capitals.append(("null", 0))
	position = 0
	for capital in capitals:
		position += 1
		if position == capital[1]:
			consecutives.append(capital[0])
		else:
			joint_capitals.append(" ".join(consecutives))
			consecutives = []
			consecutives.append(capital[0])
			position = capital[1]
	joint_capitals.remove(joint_capitals[0])
	return joint_capitals

def splitscenes(sh):
	scenes = intExt(sh)
	for i in range (len(scenes)):
		scenes[i] = intExt(sh)[i], locationslist(sh)[i], timesofday(sh)[i]
	return scenes

def intExt(sh):
	sh = sh[:]
	places = []
	for i in range(len(sh)):
		sh[i] = sh[i][0]
		places.append(sh[i])
	return places

def locationslist(sh):
	sh = sh[:]
	locations = []
	for i in range(len(sh)):
		sh[i] = sh[i][1:sh[i].index("-")]
		sh[i] = " ".join(sh[i])
		locations.append(sh[i])
	return locations
	
def timesofday(sh):
	sh = sh[:]
	times = []
	for i in range(len(sh)):
		sh[i] = sh[i][len(sh[i])-sh[i][::-1].index("-"):]
		sh[i] = " ".join(sh[i])
		times.append(sh[i])
	return times

def listDescriptions(lin):
	a = []
	b = []
	for i in range(len(lines)):
		if not (lines[i].startswith("\t") or lines[i] == '' or (lines[i].isupper() and not lines[i].endswith("."))):
			a.append([lines[i]])
			a[-1] = [i, lines[i]]
		#	descriptions_list[-1] = [i, " ".join(lines[i])]
	for i in range(len(a)-1):
		if a[i][0] == a[i+1][0]-1:
			a[i+1]=[a[i+1][0], a[i][1]+ " " + a[i+1][1]]
			a[i] = "remove"
	for x in a:
		if x != "remove":
			b.append(x)
	return b

def whoIs(name, desc): 
	d_name = name[1] #name in description
	s_name = name[2] #name when speaking
 	capitals = listCapitals(desc)
	characters = listCharacters(listCapitals(desc))
	mention = []
	l = []
	d = []
	in_description = ''
	correct = True
	for description in desc:
		if d_name in description[1]:
			named = False
			other_char_named = False
			for sentence in description[1].split("."):
				other_char_named_before = False
				if named == True:
					for character in characters:
						if (character[1] in sentence.upper() or character[2] in sentence.upper()) and character[1] != d_name:
							other_char_named = True
					if other_char_named == False:
						mention.append(sentence)
				if d_name in sentence and named == False:
					named = True
					mention.append(sentence)
				if named == False:
					for character in characters:
						if (character[1] in sentence.upper() or character[2] in sentence.upper()) and character[1] != d_name:
							other_char_named_before = True
							mention = []
					if other_char_named_before == False:
						mention.append(sentence)
			return str(".".join(mention)) + "."

	for i in range(len(l)):
	 	for j in range(l[i-1], l[i]):
	 		if (s_name in lines[j] and "\t\t\t\t" in lines[j]) or (s_name in (lines[j]).upper() and "\t\t\t" in lines[j]):
	 			if len(d[i-1])>1:
	 				return(d[i-1])
	 			else:
	 				return(d[i-2])

def whenSpeaks(name):
	number = 0
	for line in lines:
		if name in line and "\t\t\t\t" in line and "CONT" not in line:
			number += 1
	return number

def wordsSpoken(name):
	words = []
	frequency = []
	spoken = []
	diolouge = False
	some_words = ''
	for line in lines:
		some_words = ''
		if diolouge == True:
			if (not "\t\t" in line) or ("\t\t\t" in line):
				diolouge = False
			else:
				some_words = line.split(" ")
				for word in some_words:
					poss_word = word.strip('\t\t')
					poss_word = poss_word.strip('.,/;:!?-"')
					poss_word = poss_word.lower()
					if poss_word not in words and poss_word != "" and poss_word != "the":
						words.append(poss_word)
						frequency.append(1)
					elif poss_word in words:
						frequency[words.index(poss_word)]+=1
		if diolouge == False:
			if name in line and "\t\t\t\t" in line:
				diolouge = True
	for i in range(len(frequency)):
		spoken.append((words[i], frequency[i]))
	return spoken

main()
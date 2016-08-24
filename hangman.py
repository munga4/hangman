import random
words= [line.strip() for line in open("words.txt")] 

HANGMANPICS=['''
  +---+
  | |
    |  
    |
    |
    |
    |
  ==========

  ''','''

  +---+
  | |
  O |
    |
    |
    |
  ==========

  ''','''	

  +---+
  | |
   O
  | |
    |
    |
  ==========

  ''','''

  +---+
  | |
  O  |
 /| |
    |
    |
  ==========

  ''','''
  +---+
  | |
  O |
 /|\|
    |
    |
    |
  ==========

  ''','''
  __________
  |        |
  |        O
  |       /|\\
  |       /
  |
  |
  ===========

  ''','''
  
  ___________
  |          |
 /O\\        |
  |\         |
             |
             |
             |
  =========== 
  
  ''','''



  ____________
  |          |
  |          |
  |         /O\\
  |          |
  |         /|\\
  |        -----
  |        |   |
  |
  |
  |
  =============''']

def pick_a_word(words):
	word = random.choice(words)
	altered_word = list(word)
	dashes = list("_"*len(word))
	print "".join(dashes)
	return altered_word, dashes

def play():
	count=0
	while count< 8:
		guess =raw_input("Enter word")
		if guess in altered_word:
			i = len(altered_word)-1
			while i >= 0:
				if altered_word[i] == guess:
					dashes[i] = guess
					#print (word) This was to test if its picking a word.
					print "".join(dashes)

				i -= 1
		else:
			print HANGMANPICS[count]
			print('Wrong answer buddy')
			print "".join(dashes)
		if "".join(dashes) ==altered_word:
			count = 8
		count+=1
	print ('game over')
	print "The word was","".join(altered_word)


altered_word, dashes = pick_a_word(words)
play()
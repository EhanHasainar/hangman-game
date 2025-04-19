import random

words = ['aardvark', 'baboon', 'camel']

word = list(random.choice(words))
lives = 6

display = ['_']*len(word)

while lives !=0 and display!=word:
  choice = str(input('Guess a letter: ')).lower()
  print()
  if choice in word:
    for i in range(len(word)):
      if word[i] == choice:
        display[i] = choice
    print('Right Guess')
    print(display)
    print()
  else:
    lives -=1
    print('Wrong Guess')
    print(display)

if lives !=0 and display==word:
  print("You won the correct word is", word)
else:
  print()
  print("You Lost all lives")
  print()
  print('The correct word was', word)

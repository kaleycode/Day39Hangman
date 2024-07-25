import random, time, os
listOfWords = ["british","suave","accent","genius","halloween", "christmas","spaghetti","pineapple","burger","sandwich","taco"]
print("\tLet's play hangman!\n")
word = random.choice(listOfWords)
letterPicked = []
loses = 0

while True:
  
  letter = input("\tPick a letter: \n").lower()
  print()

  if letter in letterPicked:
    print("\tYou've already tried that letter")
    continue
  letterPicked.append(letter)
  
  if letter in word:
    print("\tCorrect, you found a letter!")
  else:
    print("\tNope, it's not in there.")
    loses += 1
  
  allLetters = True
  print()
  for i in word:
     if i in letterPicked:
      print(i, end="")
     else: 
      print(" _ ", end="")
      allLetters = False
  print()
  if allLetters:
    print(f"\tYou won with {7-loses} lives left!")
    break
    
  if loses == 7:
   print(f"\tYou Lose! The answer was, {word}")
   break
  else:
    print()
    print(f"\tYou have {7 - loses} lives left.")
    print()

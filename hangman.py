import random
from words import word_list

wrong_guess = 6
guess =[]
done = False
word = (random.choice(word_list)).upper()
# word = "hello"

while not done:
    for letter in word:
        if letter.upper() in guess:
            print(letter,end =" ")
        else:
            print("_",end=" ")
    print("")

    guesses = input(f"Number of Guess Left {wrong_guess}, Next Guess:")
    guess.append(guesses.upper())
    if guesses.upper() not in word.upper():
        wrong_guess -=1
        if wrong_guess == 0:
            break
    done= True
    for letter in word:
        if letter.upper() not in guess:
            done = False
if done:
    print(f"You found the word. It was {word}")
else:
    print(f"Game Over! The word was {word}")
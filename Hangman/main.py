import random
import hangman_art
from hangman_words import word_list

print(hangman_art.logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6
guesses = []

#Create blanks
display = []
for char in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in guesses:
        print(f"\nYou've already guessed {guess}\n")
    else:
        guesses.append(guess)
         #Check guessed letter
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = chosen_word[position]
        #Join all the elements in the list and turn it into a String.
                print(f"\n{' '.join(display)}\n")

          #Check if user is wrong.
        if guess not in chosen_word:
            lives -= 1
            print(f"\nYou guessed {guess}, that's not in the word.\n")
            print(f"\nYou have {lives}/6 lives left.")
            print(hangman_art.stages[lives])
            if lives == 0:
                 end_of_game = True
                 print(f"the word was {chosen_word}\n")
                 print("You lose.")

           #Check if user has got all letters.
        if "_" not in display:
            end_of_game = True
            print("You win.")

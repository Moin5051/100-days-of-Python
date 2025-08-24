import random
import hangman_words #you can also import it as "from hangman_words import word_list and then only use word_list in the code following in the page. And not use a dot each time.
import hangman_art #with the from import you can import as many in the page as you want and the choice is yours if you want to eliminate something in it. 

#Choosing the word
lives = 6
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

#Determining the Word length
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

#Starting the while loop
while not game_over:
    print(f"**************************** {lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You have already guessed this letter: {guess}")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


   #if the word is guessed or not 
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that letter is not in the word, You lose a life.")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The correct word is: {chosen_word}")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
        print(f"With {lives} Lives Remaining.")

    # Art to show
    print(hangman_art.stages[lives])

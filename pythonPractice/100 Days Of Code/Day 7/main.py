import random
import hangman_words
import hangman_art

print(hangman_art.logo)
lives = 6

chosen_word = random.choice(hangman_words.word_list)


placeholder = ""
for i in range(len(chosen_word)):
    placeholder = placeholder + "_"
print("Word to guess : " + placeholder)


game_over = False 
correct_letters = [] 



while not game_over : 
    print(f"**********************************{lives}/6 LIVES LEFT******************************")
    guess = input("Guess a letter : ").lower()

    if guess in correct_letters:
        print("You already guessed letter : "+guess)

    
    display = ""
    for letter in chosen_word:
        if letter == guess:
            display = display + letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
            correct_letters.append("_")
    print(display)

    if guess not in chosen_word:
        lives = lives -1 
        print(f"You guessed {guess}, that's not in the word you lose a life.")
        if lives == 0 :
            game_over = True
            print(f"**********************IT WAS {chosen_word} ! You lose***************************")

    if "_" not in display:
        game_over = True 
        print("*********************You win*********************")

    print(hangman_art.stages[lives])
    





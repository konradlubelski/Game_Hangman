
import random
import collections


def code_of_hangamn_game():   
    list_of_words=['victory','python','code','computer','knife','mouse','language','calculator',
    'destination','desire','scientist','mathematics','inventor','speaker','cosmos','building',
    'emergency','economy','dictionary','printer','accommodation']
    random_word=random.choice(list_of_words)
    number_of_repetitions_of_letters= collections.Counter(random_word)
    print(random_word)
    player_chances=10
    letters_to_guess = len(random_word)
    dictionary_of_letters={}
    while player_chances>0:
        input_letter=input("\nYou random a word which consist of " +str(len(random_word))+" letters. Please enter a single letter. ")
        if input_letter.isalpha()==True and len(input_letter)==1:
            if input_letter in random_word:
                if input_letter in dictionary_of_letters:
                    print("\nYou change the entered letter, because this letter was entered")
                
                else:
                    dictionary_of_letters[input_letter]={number_of_repetitions_of_letters.get(input_letter)}
                    number_of_repetitions_of_letter = number_of_repetitions_of_letters.get(input_letter)
                    letters_to_guess -= number_of_repetitions_of_letter
                    print("\nYou guessed that " + input_letter + " is in a random word.You have " + str(letters_to_guess) + " letters to guess.")
                    for index in range(len(random_word)):
                        if random_word[index]==input_letter:
                            print(random_word[index], end="")
                        else:
                            print("-", end="")
                    if letters_to_guess==0:
                        print("\nYou win! Congratulations")
                        exit()
            else :
                player_chances -=1
                print ("\nYou didn't guess the letter. You have " + str(player_chances) + " chances left.")
                if player_chances==0:
                    print("\nUnfortunately you lost. Play again")
                    exit()
                

        if input_letter.isalpha()==False or len(input_letter)!=1:
            print("\nYou didn't enter a single letter. Please try again ")
        

code_of_hangamn_game()

'''
def check_index_of_word():
    random_word="calculator"
    player_chances=5
    while player_chances>0:
        input_letter=input("Input letter")
        if input_letter in random_word:
            for index in range(len(random_word)):
                if random_word[index] == input_letter:
                    print(random_word[index])
                else:
                    print("-", end="")
                    
        else:
            print("You dont guess the letter in word")
            player_chances -=1
            print(player_chances)

    
    

check_index_of_word()
'''
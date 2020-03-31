import random
import collections
'''
def split (word):
    return[letter for letter in word]

def find_char(random_word, guess):
    list_of_position=[]
    for pos, letter in enumerate(random_word):
        if letter == guess:
            list_of_position.append(pos)
        return list_of_position

def insert_letter(word_guess, guess, pos):
    for i in range(len(pos)):
        word_guess[pos[i]] = guess
    return word_guess

def code_of_hangamn_game():   
    list_of_words=['victory','python','code','computer','knife','mouse','language','calculator',
    'destination','desire','scientist','mathematics','inventor','speaker','cosmos','building',
    'emergency','economy','dictionary','printer','accommodation']
    random_word=random.choice(list_of_words)
    number_of_repetitions_of_letters= collections.Counter(random_word)
    hidden_word="-"*len(random_word)
    print(random_word)
    random_word_split=split(random_word)
    hidden_word_split=split(hidden_word)
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
                    pos = find_char(random_word_split, input_letter)
                    wg = insert_letter(hidden_word_split, input_letter, pos)
                    print(''.join(wg))
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
    list_of_letters=[]
    for index in range(len(random_word)):
        list_of_letters.append("")
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
                            list_of_letters.pop(index)
                            list_of_letters.insert(index, input_letter)
                            print(list_of_letters)
                            # x = print(random_word[index], end="")
                        
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
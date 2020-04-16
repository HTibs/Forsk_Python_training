'''
                                HangMan Letter game
                                
computer picks a word, the player the player can guess it letter by letter, if the player is able to 
guess in the defined number of chances he/she wins or looses elsewise

Step 1 make a list of words
s2 pick a random word form the list
s3 get a guess from the player
s4 compare the guess to the secret number
s5 if the player guesses the write number print player wins
s6 or if the player cant guess it he/she looses amd computer wins

Algo:
    s1import libs
    s2 make a list of words
    s3 show message to start game
    s4 pick random word
    s5 add contition of win or loose
    s6 draw spaces, draw guessed letters, spaces, strikes
    s7 take guess
    s8 check the input from the user
    
'''

import random

words = ['apple', 'banana', 'orange', 'strawberry', 'chikoo', 'watermelon']

#take global bad guess and good guess 
bad_guess = ['a']
good_guess = []
guessed = []

def findOccurences(string, ch):
    return [i for i , letter in enumerate(string) if letter == ch]

def guess_taken(alpha, selected_word, guess_word):
    li1 = findOccurences(selected_word, alpha)
    #print(li1)
    for i in li1:
        guess_word[i]=alpha
    print(' '.join(guess_word))
    if selected_word == (''.join(guess_word)) :
        print("guessed")
        return 1
        
    
   # if(list(selected_word)==guess_word)
    
    '''for index,i in enumerate(selected_word):
        if (alpha == i):
            good_guess.append(alpha)
            guess_word[index]=alpha
            return(guess_word)
            index=index+1
            break
        index= index+1'''
    
while True:
    start = input('Enter to start or q to quit')
    if(start =='q'):
        break
    else:
        selected_word = random.choice(words)
        guess_word = list('_'*len(selected_word))
        chances = len(selected_word)+6
        print(' '.join(guess_word), "    Chances: ", chances)
        
        count =0
        while (count <=chances):
            alpha = input("Enter alphabet guess:")
            count= count+1
            if(alpha not in guessed):
                if(alpha in selected_word):
                    guessed.append(alpha)
                    ans = guess_taken(alpha, selected_word, guess_word)
                    if ans == 1:
                        break
                else:
                    print("Wrong Guess")
                    guessed.append(alpha)
                    continue
            else:
                print("Already Guessed")
                continue
        else:
            print("\nOut of Chances ")




'''

                                    importing time module
# this is called code profiling
# mainly used for time comlexity of code part

import time
def func():
    start_time = time.time()
    number=0
    
    while number<20:
        number=number+1
    end_time = time.time()
    print('func function takes', end_time-start_time, ' secs')
func()


'''


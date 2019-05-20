givenInput = "Hello2017HappyNewYear2018Is18MonthsToCome"
# longest K words in a list 
from itertools import count 
def longest_word(wordsInInput, K): 
	cnt = count() 
	return sorted(wordsInInput, key = lambda w : (len(w), next(cnt)),reverse = True)[:K] 
#print(longest_word(lst, K)) 


def charCheck(input_char):
    wordsInInput = []
    EmptyString = ''
    for i in givenInput:
        # CHECKING FOR ALPHABET
        if ((int(ord(i)) >= 65 and int(ord(i)) <= 122)):
            #print( " Alphabet ",i)
            EmptyString = EmptyString+i
        # CHECKING FOR
        elif(int(ord(i)) >= 48) and (int(ord(i)) <= 57):
            #print(" Digit ")
            wordsInInput.append(EmptyString)
            EmptyString = ''

            # OTHERWISE SPECIAL CHARACTER 
        else:
            pass
            #print(" Special Character ")
        for i in wordsInInput:
            if len(i)==0:
                wordsInInput.remove(i)
        # Driver Code 
        #input_char = '$'
        #charCheck(input_char) 
    #print(wordsInInput)
    print(longest_word(wordsInInput,2))
charCheck(givenInput)


#Credits
#https://www.geeksforgeeks.org/python-find-k-longest-words-in-given-list/
#https://www.geeksforgeeks.org/program-check-input-character-alphabet-digit-special-character/

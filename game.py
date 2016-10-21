import time
name = input("what is your name? ")
print("hello"+name,"time to play")
#wait for 1sec
time.sleep(1)
print("start guessing...")
time.sleep(1.5)

#here we see secret
word="secret"

#create a variable with an empty value

guesses=" "

#determine no. of turns

turns=10

#chesk if turn are more than 0
while(turns>0):
    #make counter that starts with 0
    failed = 0

    #for every character in secret word
    for char in word:
        #see if the char is in the players guess
        if char in guesses:
            print(char)
        else:
            #if not found print desh
            print("_")
            failed += 1
    if failed == 0:
        print("you won")
        break
    guess=input("guess a char")

    #set the players guess to guesses

    guesses += guess

    #if guess is not found in the secret word
    if guess not in word:
        #turn counter decresasr with 1
        turns -= 1
        print("wrong")

        #how many turns are
        print("you have", +turns, 'more guesses')

        #if the turns are equal to 0
        if turns == 0:
            print("you lose")
            

    

    
            

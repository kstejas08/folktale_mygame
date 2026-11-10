print("===============GEO_GUESSER!===============")
print("Your Mission is to find the mystery country!")
print("wrong answers let you try the question again")

playing=True

while playing:
    attempts=0

    # part 1 guess the planet
    correct=False
    while correct == False:
        answer=input("\nStep 1: there are 8 planets in the solar system (sorry pluto). which planet are we on? Hint: You live here! ").strip().lower()
        attempts+=1

        if answer=="earth":
            print("Correct! Meh as if there are countries on mars")
            correct=True
        elif answer=="mars":
            print("bro what are you doing on mars? ALIEN LIFE SPOTTED. try again!")
        else:
            print("Oh! you seem to be the founder of your country. pls stay there and never come back XDD. try again!")

    #part 2 guess the continent
    correct=False
    while correct == False:
        answer=input("\nStep 2: there are 7 continents on planet Earth. Which continent do you think this country belongs to? Hint: It is the largest continent! ").strip().lower()
        attempts+=1

        if answer=="asia":
            print("You are on a roll! Welcome to Asia. Let us spice up things now")
            correct=True
        elif answer=="antarctica":
            print("Silly! there are no countries in antarctica. Even a penguin knows it XDD. try again!")
        else:
            print("Incorrect! Think of the continent which has just 4 letters in it and try again!")
    
    #part 3 guess the landmark
    correct=False
    while correct == False:
        answer=input("\nStep 3: there are seven wonders of the world. Guess Any one which is located in Asia.\n Ps: One of these wonders are located in this Mysterious country!").strip().lower()
        attempts+=1

        if answer=="taj mahal" or answer=="petra" or answer=="great wall of china":
            print("You really are a Geography Nerd.. Well Done!")
            correct=True
        elif answer=="colosseum" or answer=="chichen itza" or answer=="machu picchu" or answer=="christ the redeemer":
            print("That's not located in asia.. try again! \n :( ")
        else:
            print("You just created the eight wonder of world. Lets just stick to seven XD. try again! ")
        
    #part 4 guess the flag
    correct=False
    while correct == False:
        answer=input("\nStep 4: the national flag of this country has saffron, white and green stripes.\n what shape is the central blue ashoka chakra? Hint: This shape has no edges! ").strip().lower()
        attempts+=1

        if answer=="circle":
            print("Correct! Your math skills came handy!")
            correct=True
        else:
            print("Incorrect :( \n dont worry, here is a hint for you! The shape starts with the letter c ")
        
    #part 5 the finale
    correct=False
    while correct == False:
        print("\nStep 5: Time to solve the mystery!")
        print("Quick Recap \n We got to know the country is on earth, is in asia, has one of the seven wonders of the world and a flag with the ashoka chakra!")
        answer=input("\n which country is it? ").strip().lower()
        attempts+=1

        if answer=="india":
            print("Correct! The Mystery Country was INDIA!")
            print("Case closed. You can officially call yourself a detective now XDD")
            print("total guesses:" , attempts)
            if attempts == 5:
                print("A perfect game. 5 questions, 5 answers. Well Done!")
            else:
                print("Extra guesses: ", attempts-5, "\n every detective needs practise!")
            correct=True
        
        else:
            print("one last clue.. it's capital is New Delhi. Try again ")

    answer=""
    while answer !="yes" and answer !="no":
        answer=input("\nPlay again? type Yes or No: ").strip().lower()
        if answer=="yes":
            print("same mystery, fresh detective lens! let's go again!")
        elif answer=="no":
            playing = False
        else:
            print("every detective must choose yes or no! ")


